import ast
import hashlib
import json
import os


def compute_source_hash(root_dir: str, source_dir: str) -> str:
    """MD5 of all .py files under source_dir, sorted for determinism."""
    hasher = hashlib.md5()
    source_path = os.path.join(root_dir, source_dir)
    for dir_path, dirs, filenames in os.walk(source_path):
        dirs.sort()
        for filename in sorted(filenames):
            if filename.endswith('.py'):
                filepath = os.path.join(dir_path, filename)
                hasher.update(filepath.encode())
                with open(filepath, 'rb') as f:
                    hasher.update(f.read())
    return hasher.hexdigest()


def save_cg_cache(root_dir: str, source_dir: str, source_hash: str,
                  cg_output: dict, class_manager, import_manager) -> None:
    """Write call graph + metadata to disk."""
    metadata = {"source_hash": source_hash, "source_dir": source_dir}
    with open(os.path.join(root_dir, 'cache_metadata.json'), 'w') as f:
        json.dump(metadata, f, indent=2)

    class_mro = {name: node.mro for name, node in class_manager.get_classes().items()}
    imports = {mod: list(data["imports"]) for mod, data in import_manager.import_graph.items()}
    cache_data = {"cg_output": cg_output, "class_mro": class_mro, "imports": imports}
    with open(os.path.join(root_dir, 'call_graph.json'), 'w') as f:
        json.dump(cache_data, f, indent=2)


def load_cg_cache(root_dir: str, source_dir: str, current_hash: str):
    """Return cached data dict if hash matches, else None."""
    meta_path = os.path.join(root_dir, 'cache_metadata.json')
    cg_path = os.path.join(root_dir, 'call_graph.json')
    if not os.path.exists(meta_path) or not os.path.exists(cg_path):
        return None
    try:
        with open(meta_path, 'r') as f:
            metadata = json.load(f)
        if metadata.get("source_hash") != current_hash or metadata.get("source_dir") != source_dir:
            return None
        with open(cg_path, 'r') as f:
            return json.load(f)
    except Exception:
        return None


def _analysis_cache_path(root_dir: str, model_suffix: str) -> str:
    filename = f"analysis_cache_{model_suffix}.json" if model_suffix else "analysis_cache.json"
    return os.path.join(root_dir, filename)


def save_analysis_cache(root_dir: str, source_dir: str, source_hash: str,
                        functions: dict, classes: dict, model_suffix: str = "") -> None:
    """Write per-function/per-class LLM analysis results to disk (per-model)."""
    cache_data = {
        "source_hash": source_hash,
        "source_dir": source_dir,
        "model": model_suffix,
        "functions": functions,
        "classes": classes,
    }
    with open(_analysis_cache_path(root_dir, model_suffix), 'w') as f:
        json.dump(cache_data, f, indent=2)


def load_analysis_cache(root_dir: str, source_dir: str, current_hash: str,
                        model_suffix: str = ""):
    """Return cached analysis dict if hash matches, else None."""
    path = _analysis_cache_path(root_dir, model_suffix)
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        if data.get("source_hash") != current_hash or data.get("source_dir") != source_dir:
            return None
        return data
    except Exception:
        return None


class CachedClassNode:
    def __init__(self, mro):
        self.mro = mro


class CachedImportManager:
    def __init__(self, imports_data: dict):
        self._imports = {mod: set(imports) for mod, imports in imports_data.items()}

    def get_imports(self, modname):
        return self._imports.get(modname, [])


class CachedClassManager:
    def __init__(self, class_mro_data: dict):
        self._classes = {name: CachedClassNode(mro) for name, mro in class_mro_data.items()}

    def get_classes(self):
        return self._classes


class CachedCG:
    """Lightweight stub that mimics CallGraphGenerator for post-cache usage."""
    def __init__(self, import_manager: CachedImportManager, class_manager: CachedClassManager):
        self.import_manager = import_manager
        self.class_manager = class_manager


def get_code(code: str):
    if len(code.split('```')) < 3:
        return code
    tmp = '```'.join(code.split('```')[1:-1])
    if tmp[0: 6] == 'python':
        tmp = tmp[6:]
    return tmp


def get_origin_code(file_path, start, end):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return '\n'.join(lines[start - 1: end])


def get_class_attr(node, source_code) -> str:
    class_attributes_code = []
    for stmt in node.body:
        if isinstance(stmt, ast.Assign):
            class_attr_code = ast.get_source_segment(source_code, stmt)
            class_attributes_code.append(class_attr_code)
    return "\n".join(class_attributes_code)


class ParentNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.parent_map = {}

    def visit(self, node):
        for child in ast.iter_child_nodes(node):
            self.parent_map[child] = node
        self.generic_visit(node)


def get_mod_name(entry, pkg):
    input_mod = to_mod_name(
        os.path.relpath(entry, pkg))
    if input_mod.endswith("__init__"):
        input_mod = ".".join(input_mod.split(".")[:-1])
    return input_mod


def to_mod_name(name):
    return os.path.splitext(name)[0].replace("/", ".")
