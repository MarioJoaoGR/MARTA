import glob
import os
from _ast import arg
import asyncio
import json
import re

from tqdm import tqdm
from marta.coverage_message import MyCoverage, CoverageMessage
from marta.embedding import embedder, find_topK_message, function_database

from marta.pycg.pycg import CallGraphGenerator
from marta.pycg import formats
from typing import List
from marta.gptapi import model
from marta.testcase_react import TestManager, Testcase
from marta.utils import *
from marta.recorder import recoder
from marta.config import config

from marta.react_logger import log, log_block



class ProjectMessage:
    def __init__(self, root_dir: str, source_dir: str, dir_type='Test4DT_tests'):
        self.root_dir: str = root_dir
        self.source_dir = source_dir
        self.current_round = 0  # ronda atual do loop --num (ver generate_once)

        # Raiz de import. Se source_dir for um CONTAINER (sem __init__.py — ex.:
        # ansible/lib, black/src), os módulos só são importáveis a partir de
        # root_dir/source_dir, e o mod_name (relativo a root_dir) leva o prefixo
        # do container ('lib.ansible...') que NÃO faz parte do import real. Se
        # source_dir for o próprio pacote (codetiming/), import_root == root_dir
        # e o mod_name já é o nome importável → tudo fica como estava nos 25
        # projetos normais (prefixo vazio, import_root inalterado).
        _src_full = os.path.join(self.root_dir, self.source_dir) if self.source_dir else self.root_dir
        self.source_is_container = bool(self.source_dir) and \
            not os.path.exists(os.path.join(_src_full, '__init__.py'))
        self.import_root = _src_full if self.source_is_container else self.root_dir
        self._src_prefix = (self.source_dir.replace(os.path.sep, '.').strip('.') + '.') \
            if self.source_is_container else ''


        # --- ALTERAÇÃO AQUI: Tornar a pasta de testes dinâmica ---
        safe_model = os.environ.get('SAFE_MODEL', '')
        if safe_model:
            self.dir_type: str = f"{dir_type}_{safe_model}"
        else:
            self.dir_type: str = dir_type
        # ---------------------------------------------------------
        
        self.file_messages: List[FileMessage] = []
        self.cg_edges: List[CGEdge] = []
        self.dir_message = DictionaryMessage(self.root_dir, self, None)
        self.coverage_summary = None
        self.coverage = None
        self.code_changed = True


    async def init(self):
        files: [str] = self._get_files()
        for file in files:
            self.file_messages.append(FileMessage(self.root_dir, file, self))

        source_hash = compute_source_hash(self.root_dir, self.source_dir)
        cached = load_cg_cache(self.root_dir, self.source_dir, source_hash)

        if cached is not None:
            print("🚀 [CACHE HIT] Grafo carregado com sucesso. A saltar análise estática.")
            self.code_changed = False
            output = cached["cg_output"]
            cg = CachedCG(
                CachedImportManager(cached["imports"]),
                CachedClassManager(cached["class_mro"])
            )
        else:
            print("⚠️ [CACHE MISS] Nenhuma cache válida encontrada. A iniciar análise estática (PyCG)...")
            cg = CallGraphGenerator(files, self.root_dir, -1, 'call-graph')
            cg.analyze()
            formatter = formats.Simple(cg)
            output = formatter.generate()
            save_cg_cache(self.root_dir, self.source_dir, source_hash,
                          output, cg.class_manager, cg.import_manager)

        self.analyze_function_members()
        self.complete_file_imports(cg)
        self.parseExtend(cg.class_manager.get_classes())
        self.parse_full_members()
        self.parseCG(output)

        await self.dir_message.init()

        safe_model = os.environ.get('SAFE_MODEL', '')
        analysis = load_analysis_cache(self.root_dir, self.source_dir, source_hash, safe_model)
        needs_save = False
        if analysis is not None:
            print(f"🚀 [CACHE HIT] Análise de funções/classes carregada (modelo={safe_model or 'default'}). A saltar análise LLM.")
            self.apply_analysis_cache(analysis)
        else:
            print(f"⚠️ [CACHE MISS] Sem cache de análise para modelo={safe_model or 'default'}. A analisar funções e classes (LLM)...")
            await self.analyze_functions()
            await self.get_total_what_todo()
            await self.generate_summary()
            await self.analyze_each_class()
            needs_save = True

        self.embedding_class_summary()
        function_database.init(self)

        # Inferência de tipos por parâmetro (RAG sobre as embeddings de classes).
        # Backfill em caches antigas que não tenham self.judge persistido.
        needs_judge = any(
            f.judge is None and len(f.params) > 0
            for fm in self.file_messages for f in fm.functions
        )
        if needs_judge:
            print("🔄 [PARAM TYPES] A inferir tipos de parâmetros via RAG...")
            await self.analyze_param_types()
            needs_save = True

        if needs_save:
            save_analysis_cache(self.root_dir, self.source_dir, source_hash,
                                self.collect_function_analysis(), self.collect_class_analysis(),
                                safe_model)

        self.init_test_path(self.dir_type)
        # MyCoverage usa self.root_dir como cwd do subprocess pytest (= onde o
        # PYTHONPATH aponta, para os testes encontrarem o source). Mas test_path
        # passa a ser um caminho ABSOLUTO via get_output_root(), para que o
        # coverage.json fique em Results_*/ em vez de poluir o source.
        self.coverage = MyCoverage(
            self.root_dir,
            os.path.join(get_output_root(self.root_dir), self.dir_type),
            self.source_dir,
        )


    def generate_once(self, round_num: int = 0):
        # current_round torna o [SKIP] da generate_react_flow round-aware: a ronda
        # i só salta funções que JÁ tenham > i ficheiros de teste. Antes o skip
        # disparava sempre que code_changed=False e existisse 1 ficheiro → as
        # rondas 2-3 (--num 3, protocolo Test4Py: 65.2→74.1% = +8.9pts) eram
        # no-ops em runs retomados/com cache (1901 _0 vs 138 _1 no run 16B).
        self.current_round = round_num
        asyncio.run(self.generate_test_case())
        coverage = self.coverage.get_coverage()
        recoder.score.get_coverage(coverage, self.root_dir.split(os.path.sep)[-1])
        self.coverage_summary = coverage['totals']
        for file_path, file in coverage['files'].items():
            mod_name = file_path[:-3].replace('/', '.')
            if mod_name.endswith("__init__"):
                mod_name = ".".join(mod_name.split(".")[:-1])
            file_message = self.find_file_by_mod(mod_name)
            if file_message is not None:
                for name, function in file['functions'].items():
                    for function_message in file_message.functions:
                        if function_message.func_name == name:
                            coverage_message = CoverageMessage(function['missing_lines'], function['summary'])
                            function_message.test_manager.coverage = coverage_message


    def find_file_by_mod(self, mod: str):
        for file_message in self.file_messages:
            if file_message.mod_name == mod:
                return file_message
        return None


    def get_coverage_message(self):
        covered_line = 0
        uncovered_line = 0
        covered_branch = 0
        uncovered_branch = 0
        for file_message in self.file_messages:
            for function in file_message.functions:
                if function.test_manager.coverage is None:
                    uncovered_line += function.end_line - function.start_line + 1
                else:
                    coverage: CoverageMessage = function.test_manager.coverage
                    covered_line += coverage.get_covered_lines()
                    uncovered_line += coverage.get_missing_lines()
                    covered_branch += coverage.get_covered_branches()
                    uncovered_branch += coverage.get_missing_branches()
        return covered_line, uncovered_line, covered_branch, uncovered_branch


    def _targeted_file_messages(self):
        """Return file_messages filtered by projects.json when run_benchmark=True.
        Returns the full list if filtering doesn't apply."""
        if not config.run_benchmark:
            return self.file_messages
        try:
            with open('projects.json', 'r') as f:
                projects = json.load(f)
        except FileNotFoundError:
            return self.file_messages
        project = self.root_dir.split(os.path.sep)[-1]
        if project not in projects:
            return self.file_messages
        targets = set(projects[project])
        # mod_name vem de get_mod_name(file, root_dir) → relativo ao root_dir,
        # logo inclui o source_dir como prefixo (ex.: source_dir='lib' →
        # 'lib.ansible.cli.adhoc'). Quando o source_dir é um CONTAINER (lib, src)
        # e não o próprio pacote, os módulos CM no projects.json NÃO têm esse
        # prefixo ('ansible.cli.adhoc', 'blib2to3.*') → o match exato falhava e
        # dava 0 testes (ansible, black). Casar também sem o prefixo source_dir.
        src_prefix = self.source_dir.replace(os.path.sep, '.').strip('.')
        src_prefix = (src_prefix + '.') if src_prefix else ''

        def _hit(name):
            if name in targets:
                return True
            return bool(src_prefix) and name.startswith(src_prefix) \
                and name[len(src_prefix):] in targets

        return [fm for fm in self.file_messages if _hit(fm.mod_name)]

    async def generate_test_case(self):
        targeted = self._targeted_file_messages()
        num = 0
        for file_message in targeted:
            for _ in file_message.functions:
                    num += 1
        with tqdm(total=num, desc=f"Generate test cases") as pbar:
            tasks = []
            for file_message in targeted:
                for function in file_message.functions:
                    tasks.append(self.fetch_data(function, pbar))
            await asyncio.gather(*tasks)


    async def fetch_data(self, function, pbar):
        # await function.test_manager.generate_test_case()
        await function.generate_react_flow()
       
        pbar.update(1)


    def init_test_path(self, dir_type):
        out_root = get_output_root(self.root_dir)
        # import_root == root_dir nos projetos normais; nos containers (ansible/
        # lib, black/src) é root_dir/source_dir, para os módulos serem importáveis
        # pelo nome real (ansible.cli.adhoc) e os imports internos do pacote
        # ('from ansible.x import ...') resolverem. Vale para validação, coverage
        # e re-validação (todas descobrem este conftest).
        conf_content = f"import sys\n\ndef pytest_configure(config):\n    sys.path.append(\'{self.import_root}\')"
        test_dir = out_root + os.path.sep + dir_type
        if not os.path.exists(test_dir):
            os.makedirs(test_dir, exist_ok=True)
            with open(out_root + os.path.sep + dir_type + os.path.sep + '__init__.py', 'w'):
                pass
            with open(out_root + os.path.sep + dir_type + os.path.sep + 'conftest.py', 'w') as f:
                f.write(conf_content)
        for file_message in self._targeted_file_messages():
            for function in file_message.functions:
                function.test_manager.init_test_single_path()


    def parseExtend(self, classes):
        for full_name, class_item in classes.items():
            son_class = self.get_class_by_full_name(full_name)
            if son_class is None:
                continue
            for father in class_item.mro:
                father_class = self.get_class_by_full_name(father)
                if father_class is not None:
                    son_class.father.append(father_class)


    def get_class_by_full_name(self, full_name):
        for file_message in self.file_messages:
            class_message = file_message.get_class_by_full_name(full_name)
            if class_message is not None:
                return class_message
        return None


    def _get_files(self) -> List[str]:
        files = []
        for dir_path, _, filenames in os.walk(os.path.join(self.root_dir, self.source_dir)):
            for filename in filenames:
                if filename.endswith('.py'):
                    py_path = os.path.join(dir_path, filename)
                    files.append(py_path)
        return files


    def parseCG(self, output):
        for module, calls in output.items():
            source = self.find_module(module)
            if source is None:
                continue
            for call in calls:
                dest = self.find_module(call['dest'])
                if dest is None:
                    continue
                self.cg_edges.append(CGEdge(source, dest, call['line_no']))


    def find_module(self, module_name: str):
        for file_message in self.file_messages:
            if module_name.__contains__(file_message.mod_name):
                for function_message in file_message.functions:
                    if function_message.module_name == module_name:
                        return function_message
        return None


    def find_file(self, file_path: str):
        for file_message in self.file_messages:
            if file_message.file_path == file_path:
                return file_message
        return None


    def complete_file_imports(self, cg: CallGraphGenerator):
        for file_message in self.file_messages:
            file_message.imports = self.find_files_by_module(cg.import_manager.get_imports(file_message.mod_name))


    def find_files_by_module(self, module_names: set[str]):
        files: List[FileMessage] = []
        for file_message in self.file_messages:
            if file_message.mod_name in module_names:
                files.append(file_message)
        return files


    def parse_full_members(self):
        for file_message in self.file_messages:
            file_message.parse_classes_full_members()


    def get_total_method_num(self):
        num = 0
        for file_message in self.file_messages:
            num += len(file_message.functions)
        return num


    def collect_function_analysis(self) -> dict:
        """Snapshot LLM-derived per-function fields, keyed by module_name."""
        functions = {}
        for file_message in self.file_messages:
            for function in file_message.functions:
                functions[function.module_name] = {
                    "done_what": function.done_what,
                    "what_todo": function.what_todo,
                    "summary": function.summary,
                    "judge": function.judge,
                }
        return functions

    def collect_class_analysis(self) -> dict:
        """Snapshot LLM-derived per-class fields, keyed by full_name."""
        classes = {}
        for file_message in self.file_messages:
            for class_message in file_message.classes:
                classes[class_message.full_name] = {
                    "summary": class_message.summary,
                    "how_to_use": class_message.how_to_use,
                }
        return classes

    def apply_analysis_cache(self, analysis: dict) -> None:
        """Restore cached LLM analysis into function/class objects."""
        functions = analysis.get("functions", {})
        classes = analysis.get("classes", {})
        for file_message in self.file_messages:
            for function in file_message.functions:
                cached = functions.get(function.module_name)
                if cached is not None:
                    function.done_what = cached.get("done_what")
                    function.what_todo = cached.get("what_todo")
                    function.summary = cached.get("summary")
                    function.judge = cached.get("judge")
            for class_message in file_message.classes:
                cached = classes.get(class_message.full_name)
                if cached is not None:
                    class_message.summary = cached.get("summary")
                    class_message.how_to_use = cached.get("how_to_use")

    async def analyze_functions(self):
        num = 0
        for file_message in self.file_messages:
            for _ in file_message.functions:
                num += 1
        with tqdm(total=num, desc=f"Analyze functions") as pbar:
            for file_message in self.file_messages:
                for function_message in file_message.functions:
                    await function_message.analyze_done_what()
                    pbar.update(1)


    async def get_total_what_todo(self):
        num = 0
        for file_message in self.file_messages:
            for _ in file_message.functions:
                num += 1
        with tqdm(total=num, desc=f"Analyze functions") as pbar:
            for file_message in self.file_messages:
                for function_message in file_message.functions:
                    if len(function_message.used) == 0:
                        await function_message.analyze_what_todo(function_message.find_readme(), False)
                    pbar.update(1)


    async def generate_summary(self):
        num = 0
        for file_message in self.file_messages:
            for _ in file_message.functions:
                num += 1
        with tqdm(total=num, desc=f"Analyze functions") as pbar:
            tasks = []
            for file_message in self.file_messages:
                for function_message in file_message.functions:
                    tasks.append(function_message.generate_summary(pbar))
            await asyncio.gather(*tasks)


    def analyze_function_members(self):
        for file_message in self.file_messages:
            for function_message in file_message.functions:
                function_message.analyze_function_members()


    async def analyze_each_class(self):
        num = 0
        for file_message in self.file_messages:
            for _ in file_message.classes:
                num += 2
        with tqdm(total=num, desc=f"Analyze each class") as pbar:
            tasks = []
            for file_message in self.file_messages:
                for class_message in file_message.classes:
                    tasks.append(class_message.generate_summary(pbar))
                    tasks.append(class_message.generate_how_to_use(pbar))
            await asyncio.gather(*tasks)


    def embedding_class_summary(self):
        # Embedding em lote das summaries de classe (uma passagem por chunk em
        # vez de um forward por classe). Classes sem summary ficam com
        # vector=None e são filtradas no find_topK_message.
        targets = [
            cm
            for file_message in self.file_messages
            for cm in file_message.classes
            if cm.summary is not None
        ]
        if not targets:
            return
        vectors = embedder.embed_documents([cm.summary for cm in targets])
        for cm, vec in zip(targets, vectors):
            cm.vector = vec


    async def analyze_param_types(self):
        """Eagerly populate self.judge for every function via RAG-driven
        parameter type inference. Idempotent: skips functions already judged
        or without parameters. Runs sequentially to play nice with the LLM
        rate limiter."""
        targets = [
            function
            for file_message in self.file_messages
            for function in file_message.functions
            if function.judge is None and len(function.params) > 0
        ]
        with tqdm(total=len(targets), desc="Infer parameter types (RAG)") as pbar:
            for function in targets:
                await function.judge_params()
                pbar.update(1)



class DictionaryMessage:
    def __init__(self, dir_path, project: ProjectMessage, father=None):
        self.dir_path = dir_path
        self.father = father
        self.project = project
        self.readme = None


    async def init(self):
        items = os.listdir(self.dir_path)
        for item in items:
            item_path = os.path.join(self.dir_path, item)
            if os.path.isdir(item_path):
                dictionary = DictionaryMessage(item_path, self.project, self)
                await dictionary.init()
            else:
                if item_path.endswith('.py'):
                    file_message = self.project.find_file(item_path)
                    if file_message is not None:
                        file_message.father = self
                elif item_path.endswith('README.md'):
                    with open(item_path, 'r') as f:
                        readme = f.read()
                        self.readme = await self.analyze_readme(readme)


    def find_readme(self):
        if self.readme is not None:
            return self.readme
        if self.father is not None:
            return self.father.find_readme()
        return None


    async def analyze_readme(self, readme: str):
        sys_prompt = """You are tasked with analyzing the contents of a README.md file and providing a clear, 
concise summary of what the project is about. 
The goal is to highlight the primary objectives and core functionality of the project. 
Avoid excessive details and aim for a brief summary that clearly conveys the project’s purpose in one or two short paragraphs.
"""
        user_prompt = f"""Please analyze the following README.md file and provide a summary that describes what the project aims to do.
{readme}
"""
        return await model.aask(sys_prompt, user_prompt)



class FileMessage:
    def __init__(self, root_dir: str, file_path: str, project: ProjectMessage):
        self.project = project
        self.file_path = file_path
        self.root_dir = root_dir
        self.mod_name = get_mod_name(file_path, root_dir)
        self.imports: List[FileMessage] = [self]
        self.classes: List[ClassMessage] = []
        self.functions: List[FunctionMessage] = []
        self.extract_classes_functions_with_comments(file_path)
        self.father = None

    @property
    def import_name(self):
        """Nome importável do módulo (o que vai nos imports dos testes gerados).
        Igual ao mod_name, exceto quando source_dir é um container (lib/src):
        aí tira o prefixo do container ('lib.ansible.cli.adhoc' → 'ansible.cli.
        adhoc'), porque o import_root já é root_dir/source_dir."""
        prefix = getattr(self.project, '_src_prefix', '')
        if prefix and self.mod_name.startswith(prefix):
            return self.mod_name[len(prefix):]
        return self.mod_name


    def find_readme(self):
        if self.father is not None:
            return self.father.find_readme()
        return None


    def get_class_by_full_name(self, full_name):
        for class_message in self.classes:
            if class_message.full_name == full_name:
                return class_message
        return None


    def parse_classes_full_members(self):
        for class_message in self.classes:
            class_message.parse_full_members()


    def extract_classes_functions_with_comments(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        tree = ast.parse(code, filename=file_path)
        visitor = ParentNodeVisitor()
        visitor.visit(tree)


        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self.classes.append(ClassMessage(self, node, code, self.mod_name))
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                parent = visitor.parent_map.get(node, None)
                parent_message = None
                if isinstance(parent, ast.ClassDef):
                    for class_message in self.classes:
                        if class_message.node == parent:
                            parent_message = class_message
                            break
                self.functions.append(FunctionMessage(self, node, parent_message, file_path, self.mod_name))



class ClassMessage:
    def __init__(self, file: FileMessage, node: ast.ClassDef, code: str, mod_name: str):
        self.file = file
        self.class_name = node.name
        self.docstring = ast.get_docstring(node, clean=False)
        self.class_code = self.get_class_code(node)
        self.start_line = node.lineno
        self.end_line = max(child.lineno for child in ast.walk(node) if hasattr(child, 'lineno'))
        self.class_attr_code = get_class_attr(node, code)
        self.members :List[str] = []
        self.parse_members(node)
        self.full_members = set()
        self.full_name = f"{mod_name}.{self.class_name}"
        self.father :List[ClassMessage] = []
        self.functions: List[FunctionMessage] = []
        self.node = node
        self.init_method = None
        self.summary = None
        self.how_to_use = None
        self.vector = None

    @staticmethod
    def get_class_code(class_def: ast.ClassDef):
        non_method_statements = [
            node for node in class_def.body
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        class_stub = f"class {class_def.name}:\n"
        body_source = "\n".join(
            "    " + ast.unparse(stmt).strip().replace("\n", "\n    ") for stmt in non_method_statements)
        return class_stub + body_source

    def get_code_with_summary(self):
        define_code = f"# mod: {self.file.import_name}"
        define_code += self.class_code
        for function in self.functions:
            define_code += function.get_code_with_summary() + '\n'
        return define_code

    def get_how_to_use(self):
        return self.how_to_use

    def suit_members(self, members: List[str]):
        count = 0
        for member in members:
            if member in self.full_members:
                count += 1
        return count

    async def generate_summary(self, pbar):
        sys_prompt = """You are an AI assistant skilled in analyzing Python code. 
Your task is to determine the role and purpose of a given class by analyzing its structure, methods, and usage.
Focus on explaining what responsibilities this class has, how it interacts with other components, 
and its overall contribution to the program. Provide a structured and concise summary of the inferred class functionality.
"""
        user_prompt = f"""Please analyze the role and responsibilities of this class. 
Explain its purpose, key functionalities, and how it might be used in the program. 

Here is a Python class:

{self.get_code_with_summary()}
"""
        self.summary = await model.aask(sys_prompt, user_prompt)
        pbar.update(1)

    async def generate_how_to_use(self, pbar):
        sys_prompt = """You are an expert in analyzing Python code. 
Your task is to examine the given class definition and provide a detailed explanation of how to initialize and use this class. 
Your response should include:

1. **Class Initialization**: Explain how to properly instantiate the class, listing the required and optional parameters in the constructor (`__init__` method).
2. **Key Methods and Attributes**: Summarize the main methods and attributes of the class, highlighting their usage.
3. **Example Usage**: Provide a Python code snippet demonstrating how to create an instance of the class and interact with its methods.

Always assume that the user wants a clear and concise explanation suitable for someone who understands Python but may not be familiar with the specific class.
"""
        user_prompt = f"""Please analyze the role and responsibilities of this class. 
Explain its purpose, key functionalities, and how it might be used in the program. 

Here is the Python class definition:

```python
{self.get_code_with_summary()}
"""
        self.how_to_use = await model.aask(sys_prompt, user_prompt)
        pbar.update(1)


    def parse_members(self, node: ast.ClassDef):
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                if item.name == "__init__":
                    for stmt in item.body:
                        if isinstance(stmt, ast.Assign):
                            for target in stmt.targets:
                                if isinstance(target, ast.Attribute) and isinstance(target.value,
                                                                                    ast.Name) and target.value.id == "self":
                                    self.members.append(target.attr)
                else:
                    self.members.append(item.name)
            elif isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        self.members.append(target.id)
            elif isinstance(item, ast.AnnAssign):
                if isinstance(item.target, ast.Name):
                    self.members.append(item.target.id)

    def parse_full_members(self):
        self.full_members = set(self.members)
        for fa in self.father:
            if fa != self:
                self.full_members.union(fa.parse_full_members())
        return self.full_members


class FunctionMessage:
    builtin_members = set(dir(object))

    def __init__(self, file: FileMessage, node: ast.FunctionDef, parent: ClassMessage, file_path: str, module_name: str):
        self.file =file
        self.node: ast.FunctionDef = node
        self.func_name = node.name
        self.parent = parent
        self.class_name = None
        if parent is not None:
            self.class_name = parent.class_name
            parent.functions.append(self)
            if self.func_name == '__init__':
                parent.init_method = self
            self.func_name = f"{self.class_name}.{self.func_name}"

        self.docstring = ast.get_docstring(node, clean=False)
        self.start_line = node.lineno
        self.end_line = max(child.lineno for child in ast.walk(node) if hasattr(child, 'lineno'))
        self.standard_code = ast.unparse(node)
        self.code = get_origin_code(file_path, self.start_line, self.end_line)
        self.module_name = f"{module_name}.{self.func_name}"
        self.uses: List[CGEdge] = []
        self.used: List[CGEdge] = []

        self.done_what = None
        self.what_todo = None
        self.summary = None
        self.params: List[ArgMessage] = []
        self.judge = None
        self.test_manager = TestManager(self, self.file.project.dir_type)


    def get_code_with_summary(self):
        return f"""
\"\"\"
{self.summary}
\"\"\"
{self.code}
"""


    def get_code_with_tests_or_summary(self):
        test_code = self.test_manager.get_first_testcase()
        if test_code == "":
            return self.get_source_code()
        else:
            return f"""{self.module_name} code:
{self.code}

test case:
{test_code}
"""


    async def generate_summary(self, pbar):
        sys_prompt = """You are an AI assistant skilled in analyzing and generating comprehensive function documentation. 
Your task is to integrate two different perspectives of docstrings—one describing what the function does (implementation perspective) 
and the other describing what the function is intended to do (requirement perspective)—along with the function's source code to generate a final, 
well-structured docstring.

Your output must:
1. Preserve and merge the key information from both docstrings.
2. Clearly describe how to use the function, including its purpose, parameters, and return values.
3. Provide insights into the function’s significance within the broader context of the codebase.
4. Use clear, precise, and professional language.
5. Let's think step by step, only output the docstring content. Do not include the source code or any extra explanations.

Now, await the user’s input containing:
- The function’s source code.
- The "what it does" docstring.
- The "what it is intended to do" docstring.
Generate the final docstring accordingly.
"""
        user_prompt = f"""Here is a function along with two docstrings from different perspectives:

### Function Source Code:
```python
{self.get_source_code()}

### "What it does" Docstring:
{self.done_what}

### "What it is intended to do" Docstring:
{self.what_todo}
"""
        self.summary = await model.aask(sys_prompt, user_prompt)
        pbar.update(1)


    def find_readme(self):
        return self.file.find_readme()


    def get_source_code(self):
        source_code = ""
        if self.parent is not None:
            source_code += f"{self.parent.class_code}\n"
            if self.parent.init_method is not None:
                if self.parent.init_method.summary is not None:
                    source_code += "\"\"\"\n" + self.parent.init_method.summary + "\n\"\"\"\n"
                source_code += self.parent.init_method.code + '\n\n'
        if self.summary is not None:
            source_code += "\"\"\"\n" + self.summary + "\n\"\"\"\n"
        if self.judge is not None:
            source_code += "\"\"\"\n" + self.judge + "\n\"\"\"\n"
        source_code += self.code
        return source_code


    def analyze_function_members(self):
        params = [arg for arg in self.node.args.args]
        try:
            for arg in getattr(self.node.args, 'posonlyargs', []):
                if arg.arg not in params:
                    params.append(arg)
            for arg in self.node.args.kwonlyargs:
                if arg.arg not in params:
                    params.append(arg)
            if self.node.args.vararg:
                if self.node.args.vararg not in params:
                    params.append(self.node.args.vararg)
            if self.node.args.kwarg:
                if self.node.args.kwarg not in params:
                    params.append(self.node.args.kwarg)
        except Exception as e:
            print("Arg parse error: ", e)

        param_members = {param.arg: {'members': set(), 'node': param} for param in params}
        param_names = [arg.arg for arg in params]

        for node in ast.walk(self.node):
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name):
                    param = node.value.id
                    if param in param_names:
                        if node.attr not in self.builtin_members:
                            param_members[param]['members'].add(node.attr)

        for param_name, param_members in param_members.items():
            self.params.append(ArgMessage(param_name, self.get_source_code(), self.summary,
                                          param_members['members'], param_members['node'], self))


    async def analyze_done_what(self):
        if self.done_what is not None:
            return self.done_what
        self.done_what = ""
        call_message = ""
        for use in self.uses:
            dest: FunctionMessage = use.dest
            done_what = await dest.analyze_done_what()
            if len(done_what) > 0:
                call_message += f"\n{dest.func_name}: \n{done_what}\n"
        source_code = self.get_source_code()
        if call_message != "":
            sys_prompt = "You are a helpful assistant designed to analyze Python functions. \
Based on the provided source code of a function and the docstrings of the other functions it calls, \
your task is to generate a clear and concise docstring for the given function. \
The generated docstring should describe what the function does, what parameters it accepts, highlighting the role of each parameter and how changes to their values affect the function’s execution. \
what it returns (if anything), and how to use the function effectively. \
Let's think step by step, only output the docstring content. Do not include the source code or any extra explanations."
            user_prompt = f"Here is the source code of a Python function and the docstrings of the functions it calls. \
Please analyze this and generate an appropriate docstring for the provided function. \
Be sure to explain what the function does and include examples or instructions on how to use it.\n\n\
source code: \n{source_code}\n\n functions it calls: \n{call_message}"
        else:
            sys_prompt = "You are a helpful assistant designed to analyze Python functions. \
Based on the provided source code of a function, \
your task is to generate a clear and concise docstring for the given function. \
The generated docstring should describe what the function does, what parameters it accepts, highlighting the role of each parameter and how changes to their values affect the function’s execution.  \
what it returns (if anything), and how to use the function effectively. \
Let's think step by step, only output the docstring content. Do not include the source code or any extra explanations."
            user_prompt = f"Here is the source code of a Python function. \
Please analyze this and generate an appropriate docstring for the provided function. \
Be sure to explain what the function does and include examples or instructions on how to use it.\n\n\
source code: \n{source_code}\n\n functions it calls: \n{call_message}"
        self.done_what = await model.aask(sys_prompt, user_prompt)
        return self.done_what


    async def analyze_what_todo_by_readme(self, readme):
        if readme is not None:
            sys_prompt = """You are an AI assistant specialized in analyzing Python code. 
Your task is to examine the given function and generate a concise and clear docstring that describes its purpose and usage. 
Consider the overall project objective to provide context, but focus on the function itself. 
If the function interacts with other parts of the project, briefly mention relevant dependencies without excessive details. 
Your output should be formatted as a Python docstring.
Let's think step by step, only output the docstring content. Do not include the source code or any extra explanations.
"""
            user_prompt = f"""Analyze the function and generate a docstring that clearly describes its purpose, parameters, 
return values, and usage. Ensure the docstring is informative yet concise.
    
**Project Overview:**
{readme}
    
**Function Source Code:**
```python
\"\"\"
{self.what_todo}
\"\"\"
{self.code}
"""
        else:
            sys_prompt = """You are an AI assistant that analyzes Python functions and provides a concise docstring 
summarizing their purpose and usage. The docstring should follow standard Python conventions, 
including a brief description, parameters, and return values if applicable. 
Maintain clarity and precision while avoiding unnecessary details.
Let's think step by step, only output the docstring content. Do not include the source code or any extra explanations.
"""
            user_prompt = f"""Here is a Python function. 
Please analyze its purpose and provide a docstring that describes what it does and how to use it. 
Ensure the docstring follows proper formatting.
            
```python
\"\"\"
{self.what_todo}
\"\"\"
{self.code}
"""
        return await model.aask(sys_prompt, user_prompt)


    async def analyze_what_todo(self, what_todo, is_judge: bool):
        if is_judge:
            self.what_todo = what_todo
        else:
            self.what_todo = await self.analyze_what_todo_by_readme(what_todo)

        for use in self.uses:
            dest: FunctionMessage = use.dest
            if dest.what_todo is None:
                sys_prompt = """You are a Python code analysis assistant.
Your task is to analyze a function call in the provided source code and produce a precise docstring that describes:
The purpose of the called function.
The semantic roles and exact parameter types, inferred from the call context and callee behavior.
The types must be as specific as possible (e.g., List[User], Dict[str, int], Optional[Config]) rather than generic types like list or dict.
Infer parameter types based on their usage and data flow, not just their names.

Output only the docstring content — do not include the source code or any extra explanations.
Think step by step before writing the final docstring."""
                user_prompt = f"""Identify the purpose of the called function {dest.func_name} and explain how to use it, formatted as a Python docstring.
Source Code:
\"\"\"
{self.what_todo}
\"\"\"
{self.code}
    
Function Call:
At line {use.line_no}, the function call of function {dest.func_name} occurs:
{use.call_code}
"""
                call_what_todo = await model.aask(sys_prompt, user_prompt)
                await dest.analyze_what_todo(call_what_todo, True)


    async def judge_params(self):
        if self.judge is not None or len(self.params) == 0:
            return
        sys_prompt = """You are an AI assistant skilled in understanding and generating Python code. 
Your task is to analyze a given function and determine how it should be called. 
You will receive the function's source code and its parameter information. 
Based on this, you must infer the appropriate way to call the function and generate example calls.

Provide clear and well-structured example calls that reflect typical usage of the function. 
If necessary, infer reasonable argument values based on parameter names and types. 
Ensure that your responses are concise and precise, avoiding redundant explanations.
"""
        user_prompt = f"""Here is a Python function along with its parameter information. 
Please analyze how this function should be called and provide example calls.

Function source code:

{self.get_source_code()}

params:
"""
        for param in self.params:
            user_prompt += await param.get_type_help()
        self.judge = await model.aask(sys_prompt, user_prompt)


        # --- ADICIONAR ESTE MÉTODO NOVO ---
    # EM test4dt/message_react.py - DENTRO DE FunctionMessage

    async def generate_react_flow(self):
        coverage_info = "First pass: Try to achieve maximum coverage."
        if hasattr(self.test_manager, 'coverage') and self.test_manager.coverage is not None:
            if len(self.test_manager.coverage.missing_lines) > 0:
                coverage_info = f"MISSING LINES TO COVER: {self.test_manager.coverage.format_missing_lines()}"
            else:
                return

        # Idempotência + nomenclatura por ronda. Cada ronda escreve UM ficheiro
        # combinado '<prefixo>_<ronda>.py' (ronda = nº de ficheiros já existentes),
        # por isso rondas posteriores acumulam cobertura em vez de sobrescrever.
        # Se o código não mudou e já existem testes, salta a geração (custo zero).
        react_prefix = self.test_manager.get_react_prefix()
        existing = sorted(glob.glob(f"{react_prefix}_*.py"))
        # SKIP round-aware: a ronda i (0-based) só salta se esta função já tiver
        # MAIS de i ficheiros (i.e., a ronda i já produziu o dela). Resume-safe:
        # num restart, as rondas re-percorridas saltam ficheiros já feitos e a
        # geração retoma exatamente na ronda interrompida. O skip antigo
        # (`existing` não-vazio → return) matava as rondas 2-3 nos runs com
        # cache/retomados: funções meio-cobertas nunca eram re-atacadas.
        current_round = getattr(self.file.project, 'current_round', 0)
        if not self.file.project.code_changed and len(existing) > current_round:
            print(f"[SKIP] Testes para '{self.func_name}' já existem (ronda {current_round}), a saltar...")
            for filepath in existing:
                self.test_manager.testcases.append(
                    Testcase.load_existing(self.test_manager, self, filepath)
                )
            return
        combined_path = f"{react_prefix}_{len(existing)}.py"

        # self.judge é populado eagerly em ProjectMessage.init via analyze_param_types
        # (RAG sobre embeddings de classes). Aqui só lê.

        # RAG ao nível de função: procura funções semanticamente parecidas
        # no projeto e fornece-as ao Planner como inspiração de cenários.
        related_block = ""
        rag_query = self.summary or self.done_what
        if rag_query:
            candidates = await asyncio.to_thread(function_database.query, rag_query, 4)
            related = [f for f in candidates if f.module_name != self.module_name][:3]
            if related:
                related_lines = ["RELATED FUNCTIONS IN THIS PROJECT (for inspiration):"]
                for rf in related:
                    snippet = (rf.done_what or rf.summary or "no summary")
                    snippet = " ".join(snippet.split())[:200]
                    related_lines.append(f"        - {rf.func_name}: {snippet}")
                related_block = "\n        " + "\n        ".join(related_lines)

        # 1. Agrega o Contexto Rico
        context_block = f"""
        Function Name: {self.func_name}
        Module: {self.file.import_name}

        SOURCE CODE:
        {self.get_source_code()}

        DOCSTRING SUMMARY:
        {self.done_what if self.done_what else "No summary available."}

        COVERAGE FEEDBACK:
        {coverage_info}
        {related_block}
        """

        # ========================================================
        # 🕵️ AGENTE 1: PLANNER
        # ========================================================
        sys_prompt_plan = "You are a QA Lead. Analyze the function and output a Test Plan in JSON format."
        user_prompt_plan = f"""
        Analyze the following function and generate a comprehensive test plan.
        
        CONTEXT:
        {context_block}
        
        TASK:
        Generate 3 distinct test scenarios covering:
        CRITICAL: If 'MISSING LINES TO COVER' are provided in the context, you MUST design these scenarios specifically to execute those missing lines.
        1. Valid inputs (Happy Path)
        2. Edge cases (e.g., None, empty lists, boundary values)
        3. Invalid inputs/Error handling
        
        SETUP GUIDANCE: prefer REAL objects with simple concrete values in 'setup';
        only suggest mocking for true external I/O (network, filesystem, subprocess).

        OUTPUT FORMAT:
        Return ONLY a raw JSON list. No Markdown. No Explanations.
        Example:
        [
            {{"name": "test_valid_case", "desc": "Test standard input", "setup": "Real instance of X with minimal args"}},
            {{"name": "test_error_case", "desc": "Test raising ValueError", "setup": "None"}}
        ]
        """
        
        raw_plan = await model.aask(sys_prompt_plan, user_prompt_plan)
        
        # Parser JSON Robusto
        try:
            # Limpa markdown se existir
            clean_json = raw_plan.replace("```json", "").replace("```", "").strip()
            start = clean_json.find('[')
            end = clean_json.rfind(']')
            
            if start != -1 and end != -1:
                final_json = clean_json[start:end+1]
                test_plan = json.loads(final_json)
                
                # log("PLANNER", f"Plano gerado com sucesso: {len(test_plan)} cenários.")
                # log_block("PLANO JSON", json.dumps(test_plan, indent=2))
            else:
                raise ValueError("JSON block not found")
        except Exception as e:
            # log("PLANNER", f"⚠️ Falha no JSON: {e}")
            # log("PLANNER", "-> A usar fallback (Teste Básico).")
            test_plan = [{"name": f"test_{self.func_name.replace('.','_')}_basic", "desc": "Basic functionality", "setup": "None"}]


        # ========================================================
        # 👷 AGENTE 2: DEV — 1 ficheiro com TODOS os cenários + self-healing
        # ========================================================
        # Antes: 1 chamada LLM por cenário (+ até 3 de cura cada) → 4-10 chamadas.
        # Agora: 1 chamada gera o ficheiro inteiro; self-healing cura o ficheiro
        # todo; no fim, salva os testes que passam (Opção D). Caminho feliz = 2
        # chamadas (Planner + Dev) em vez de 4+.
        scenarios_block = "\n".join(
            f"          {i+1}. {s.get('name')}: {s.get('desc')} (setup: {s.get('setup')})"
            for i, s in enumerate(test_plan)
        )

        max_attempts = 3
        last_error = None
        last_results = {}
        combined_tc = None
        success = False

        for attempt in range(max_attempts):
            if attempt == 0:
                instruction = (
                    f"Write a SINGLE pytest file containing ONE test function for EACH of "
                    f"these {len(test_plan)} scenarios:\n{scenarios_block}"
                )
            else:
                # RAG dirigido ao erro: funções semanticamente parecidas + (se
                # existir) um teste já validado dessa função como exemplo.
                similar_help = ""
                if last_error:
                    candidates = await asyncio.to_thread(function_database.query, last_error[:400], 3)
                    similar = [f for f in candidates if f.module_name != self.module_name][:2]
                    if similar:
                        blocks = ["SIMILAR TESTED FUNCTIONS THAT MIGHT HELP:"]
                        for sf in similar:
                            summary_line = " ".join((sf.done_what or "no summary").split())[:200]
                            blocks.append(f"- {sf.func_name}: {summary_line}")
                            tcs = getattr(sf.test_manager, 'testcases', [])
                            if tcs:
                                try:
                                    with open(tcs[0].test_path, 'r', encoding='utf-8') as f:
                                        example = f.read()[:400]
                                    blocks.append(f"  Example passing test:\n  ```python\n{example}\n  ```")
                                except (FileNotFoundError, IOError, OSError):
                                    pass
                        similar_help = "\n\n" + "\n".join(blocks)
                instruction = (
                    f"PREVIOUS CODE FAILED.\nERROR MESSAGE:\n{last_error}"
                    f"{similar_help}\n"
                    f"TASK: Rewrite the ENTIRE test file to fix this error. "
                    f"Keep one independent test function per scenario."
                )

            sys_prompt_dev = "You are a Pytest Expert. Write valid python code."
            user_prompt_dev = f"""
            {instruction}

            FUNCTION CODE:
            {self.get_source_code()}

            RULES:
            1. Output ONLY python code in ```python``` block (a complete test file).
            2. Import correctly from module '{self.file.import_name}'.
            3. Write one independent, function-based pytest test per scenario.
            4. AVOID MOCKS unless strictly necessary: prefer constructing REAL objects with simple values. Only mock true external I/O (network, filesystem, subprocess, environment). NEVER mock the module under test, plain data classes, or anything you can instantiate directly. A wrong mock fails the test without testing anything.
            5. IF you must mock, use `unittest.mock.patch` as a context manager (with patch(...):) or the `monkeypatch` fixture. NEVER assign mock objects directly to global modules (e.g., do NOT do `module.config = Mock()`). NEVER assert on mock internals (call counts of magic methods). Strict state isolation is mandatory.
            6. ASSERTIONS: keep each test focused — 1 to 2 assertions per test function, asserting CONCRETE expected values you derived from the source code. Prefer several small tests over one test with many assertions (one wrong assertion kills the whole test).
            """

            code_response = await model.aask(sys_prompt_dev, user_prompt_dev)
            clean_code = get_code(code_response)

            success, last_error, last_results, combined_tc = \
                await self.test_manager.inject_combined_test(clean_code, combined_path)
            if success:
                break

        # Opção D: se o ficheiro não passou inteiro, salva os testes que passaram
        # e revalida; se mesmo assim não passar tudo, vai inteiro para quarentena.
        if not success and combined_tc is not None:
            survivors = combined_tc.salvage_passing_tests(last_results)
            if survivors > 0:
                ok, _results, _out = combined_tc.run_pytest_with_results()
                if ok:
                    self.test_manager.testcases.append(combined_tc)
                    recoder.score.add_assertion_fix_success()
                else:
                    combined_tc.delete()
            else:
                combined_tc.delete()

class CGEdge:
    def __init__(self, source: FunctionMessage, dest: FunctionMessage, line_no: int):
        self.source: FunctionMessage = source
        self.dest: FunctionMessage = dest
        self.line_no = line_no
        self.call_code = self.get_call_code()
        self.add_use()

    def get_call_code(self):
        code_lines = self.source.code.splitlines()
        if len(code_lines) <= self.line_no - self.source.start_line or self.line_no < self.source.start_line:
            return "Not found"
        return code_lines[self.line_no - self.source.start_line]

    def add_use(self):
        self.dest.used.append(self)
        has_appeared = False
        for use in self.source.uses:
            if use.dest == self.dest:
                has_appeared = True
        if not has_appeared:
            self.source.uses.append(self)


class ArgMessage:
    def __init__(self, name, code, summary, members, node: arg, func: FunctionMessage):
        self.func: FunctionMessage = func
        self.node: arg = node
        self.name = name
        self.code = code
        self.summary = summary
        self.members = members
        self.meaning = None
        self.vector = None
        self.is_user_defined = None
        self.extract_type: str = ""


    async def get_type_help(self):
        return f"""
{self.name}: 

{await self.get_type_message()}
"""


    async def get_type_message(self):
        if self.node.type_comment is not None:
            for import_file in self.func.file.imports:
                for class_message in import_file.classes:
                    if (self.node.type_comment == class_message.class_name or
                            '['+class_message.class_name+']' in self.node.type_comment):
                        return class_message.get_how_to_use()
            self.extract_type = self.node.type_comment
            return self.node.type_comment

        if self.is_user_defined is None:
            self.is_user_defined = await self.judge_type()
        if self.is_user_defined:
            if self.meaning is None:
                self.meaning = await self.generate_meaning()
                self.vector = await asyncio.to_thread(embedder.embed_query, self.meaning)
            return self.find_type_by_RAG()
        return "build-in type"


    def find_type_by_RAG(self):
        classes = self.filter_by_members()
        found_classes = find_topK_message(self.func.file.file_path+self.func.func_name+self.name, classes, self.vector, 3)
        # TODO: change to choose on from k
        result = ""
        for found_class in found_classes:
            result += found_class.file.mod_name + '\n' + found_class.get_how_to_use() + '\n'
        return result


    def filter_by_members(self) -> List[ClassMessage]:
        max_score = 0
        suitable_classes: List[ClassMessage] = []
        for file_message in self.func.file.project.file_messages:
            for class_message in file_message.classes:
                score = class_message.suit_members(self.members)
                if score == max_score:
                    suitable_classes.append(class_message)
                elif score > max_score:
                    max_score = score
                    suitable_classes = [class_message]
        return suitable_classes


    async def generate_meaning(self):
        sys_prompt = """You are an AI assistant skilled in analyzing Python code. 
Your task is to determine the role and purpose of a class based on how its instance is used as a parameter in a given function. 
Focus on analyzing what responsibilities this class might have, how it contributes to the function’s behavior, 
and what role it likely plays in the overall program. Provide a structured and concise summary of the inferred class functionality.
"""
        user_prompt = f"""The parameter I want to analyze is {self.name}. 
Based on how this parameter is used in the function, infer the possible role and responsibilities of its class. 
        
Here is a Python function:
```python
\"\"\"
{self.summary}
\"\"\"
{self.code}
"""
        return await model.aask(sys_prompt, user_prompt)


    async def judge_type(self):
        sys_prompt = """You are an expert in Python type analysis. 
Your task is to determine whether a given function parameter belongs to a built-in type, 
a third-party library type, or a user-defined type.  

Classification rules:  
- If the parameter type is a built-in Python type (e.g., `int`, `str`, `list`), output `<1>`.  
- If the parameter type is from a third-party library (e.g., `ast.FunctionCall`), output `<2>`.  
- If the parameter type is a user-defined type (a custom class written by the user), output `<3>`.  

The user will provide a function definition and specify a parameter name. 
Respond with only the corresponding classification tag (`<1>`, `<2>`, or `<3>`) without any additional text.
"""
        user_prompt = f"""
Determine the classification of the parameter named {self.name} based on its usage in the function body.

```python
\"\"\"
{self.summary}
\"\"\"
{self.code}
"""
        return not (await model.aask(sys_prompt, user_prompt)).__contains__('<1>')
 