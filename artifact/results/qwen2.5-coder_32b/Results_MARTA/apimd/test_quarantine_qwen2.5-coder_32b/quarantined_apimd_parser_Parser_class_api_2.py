
import pytest
from ast import parse, ClassDef, AnnAssign, Assign, Delete, Name, expr, stmt
from apimd.parser import Parser





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_class_api _____________________________

    def test_valid_class_api():
        """Test class_api with a valid class definition."""
        p = Parser()
        source_code = """
    class MyClass(BaseClass):
        attr1: int
        attr2 = 42
        def method(self):
            pass
    """
        tree = parse(source_code)
        for node in tree.body:
            if isinstance(node, ClassDef):
>               p.class_api(
                    root='my_project',
                    name=node.name,
                    bases=node.bases,
                    body=node.body
                )

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'MyClass'
bases = [<ast.Name object at 0x7fb3dd11fb80>]
body = [<ast.AnnAssign object at 0x7fb3dd11fb50>, <ast.Assign object at 0x7fb3dd11fcd0>, <ast.FunctionDef object at 0x7fb3dd11fc40>]

    def class_api(self, root: str, name: str, bases: list[expr],
                  body: list[stmt]) -> None:
        """Create class API."""
        r_bases = [self.resolve(root, d) for d in bases]
        if r_bases:
>           self.doc[name] += table("Bases", items=map(code, r_bases))
E           KeyError: 'MyClass'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:456: KeyError
_____________________________ test_class_with_enum _____________________________

    def test_class_with_enum():
        """Test class_api with a class that has enum members."""
        p = Parser()
        source_code = """
    class MyClass(enum.Enum):
        attr1 = 1
        attr2 = 2
    """
        tree = parse(source_code)
        for node in tree.body:
            if isinstance(node, ClassDef):
>               p.class_api(
                    root='my_project',
                    name=node.name,
                    bases=node.bases,
                    body=node.body
                )

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'MyClass'
bases = [<ast.Attribute object at 0x7fb3dcfd3460>]
body = [<ast.Assign object at 0x7fb3dcfd3520>, <ast.Assign object at 0x7fb3dcfd3490>]

    def class_api(self, root: str, name: str, bases: list[expr],
                  body: list[stmt]) -> None:
        """Create class API."""
        r_bases = [self.resolve(root, d) for d in bases]
        if r_bases:
>           self.doc[name] += table("Bases", items=map(code, r_bases))
E           KeyError: 'MyClass'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:456: KeyError
______________________ test_class_with_deleted_attributes ______________________

    def test_class_with_deleted_attributes():
        """Test class_api with a class that has deleted attributes."""
        p = Parser()
        source_code = """
    class MyClass:
        attr1: int
        attr2 = 42
        def method(self):
            pass
    
        del attr1
    """
        tree = parse(source_code)
        for node in tree.body:
            if isinstance(node, ClassDef):
>               p.class_api(
                    root='my_project',
                    name=node.name,
                    bases=node.bases,
                    body=node.body
                )

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py:65: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'MyClass', bases = []
body = [<ast.AnnAssign object at 0x7fb3dd046590>, <ast.Assign object at 0x7fb3dd046260>, <ast.FunctionDef object at 0x7fb3dd046d40>, <ast.Delete object at 0x7fb3dd0476a0>]

    def class_api(self, root: str, name: str, bases: list[expr],
                  body: list[stmt]) -> None:
        """Create class API."""
        r_bases = [self.resolve(root, d) for d in bases]
        if r_bases:
            self.doc[name] += table("Bases", items=map(code, r_bases))
        is_enum = any(map(lambda s: s.startswith('enum.'), r_bases))
        mem = {}
        enums = []
        for node in walk_body(body):
            if isinstance(node, AnnAssign) and isinstance(node.target, Name):
                attr = node.target.id
                if is_enum:
                    enums.append(attr)
                elif is_public_family(attr):
                    mem[attr] = self.resolve(root, node.annotation)
            elif (
                isinstance(node, Assign)
                and len(node.targets) == 1
                and isinstance(node.targets[0], Name)
            ):
                attr = node.targets[0].id
                if is_enum:
                    enums.append(attr)
                elif is_public_family(attr):
                    if node.type_comment is None:
                        mem[attr] = const_type(node.value)
                    else:
                        mem[attr] = node.type_comment
            elif isinstance(node, Delete):
                for d in node.targets:
                    if not isinstance(d, Name):
                        continue
                    attr = d.id
                    mem.pop(attr, None)
                    if attr in enums:
                        enums.remove(attr)
        if enums:
            self.doc[name] += table("Enums", items=enums)
        elif mem:
>           self.doc[name] += table('Members', 'Type', items=(
                (code(n), code(mem[n])) for n in sorted(mem)))
E           KeyError: 'MyClass'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:491: KeyError
___________________________ test_invalid_class_name ____________________________

    def test_invalid_class_name():
        """Test class_api with an invalid class name."""
        p = Parser()
        source_code = """
    class 123Invalid:
        attr1: int
    """
>       tree = parse(source_code)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py:82: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = '\nclass 123Invalid:\n    attr1: int\n', filename = '<unknown>'
mode = 'exec'

    def parse(source, filename='<unknown>', mode='exec', *,
              type_comments=False, feature_version=None):
        """
        Parse the source into an AST node.
        Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
        Pass type_comments=True to get back type comments where the syntax allows.
        """
        flags = PyCF_ONLY_AST
        if type_comments:
            flags |= PyCF_TYPE_COMMENTS
        if isinstance(feature_version, tuple):
            major, minor = feature_version  # Should be a 2-tuple.
            assert major == 3
            feature_version = minor
        elif feature_version is None:
            feature_version = -1
        # Else it should be an int giving the minor version for 3.x.
>       return compile(source, filename, mode, flags,
                       _feature_version=feature_version)
E         File "<unknown>", line 2
E           class 123Invalid:
E                   ^
E       SyntaxError: invalid decimal literal

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:50: SyntaxError
___________________________ test_invalid_base_class ____________________________

    def test_invalid_base_class():
        """Test class_api with an invalid base class."""
        p = Parser()
        source_code = """
    class MyClass(InvalidBase):
        attr1: int
    """
        tree = parse(source_code)
        for node in tree.body:
            if isinstance(node, ClassDef):
                # This should not raise a SyntaxError but rather be handled gracefully
                with pytest.raises(ValueError):
>                   p.class_api(
                        root='my_project',
                        name=node.name,
                        bases=node.bases,
                        body=node.body
                    )

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py:106: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', name = 'MyClass'
bases = [<ast.Name object at 0x7fb3dd044c10>]
body = [<ast.AnnAssign object at 0x7fb3dd0450f0>]

    def class_api(self, root: str, name: str, bases: list[expr],
                  body: list[stmt]) -> None:
        """Create class API."""
        r_bases = [self.resolve(root, d) for d in bases]
        if r_bases:
>           self.doc[name] += table("Bases", items=map(code, r_bases))
E           KeyError: 'MyClass'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:456: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py::test_valid_class_api
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py::test_class_with_enum
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py::test_class_with_deleted_attributes
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py::test_invalid_class_name
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_class_api_2.py::test_invalid_base_class
============================== 5 failed in 0.14s ===============================
"""