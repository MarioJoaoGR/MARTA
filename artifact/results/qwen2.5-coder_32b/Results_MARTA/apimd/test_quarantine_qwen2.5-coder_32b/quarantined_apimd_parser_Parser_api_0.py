
import pytest
from ast import parse, FunctionDef, ClassDef
from apimd.parser import Parser

def _m(root: str, prefix: str, name: str) -> str:
    """Helper function to create a full name."""
    return f"{root}.{prefix}{name}" if prefix else f"{root}.{name}"

def esc_underscore(name: str) -> str:
    """Escape underscores in the name."""
    return name.replace('_', '\\_')

def code(s: str) -> str:
    """Format string as code."""
    return f"`{s}`"

def table(title: str, items: list[str]) -> str:
    """Create a Markdown table."""
    return f"### {title}\n\n| Item |\n|------|\n" + "\n".join(f"| {item} |" for item in items)

def doctest(docstring: str) -> str:
    """Format docstring."""
    return f"> {docstring}"

def get_docstring(node) -> str:
    """Extract docstring from node."""
    return getattr(node, 'docstring', None)

def walk_body(body):
    """Walk through the body of a class or function."""
    for e in body:
        yield e

# Test cases


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_api_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_happy_path ________________________________

    def test_happy_path():
        source_code = """
    def my_function(param1):
        \"\"\"This is a function docstring.\"\"\"
        return param1 * 2
    
    class MyClass:
        def __init__(self, value):
            self.value = value
    
        def method(self):
            pass
    """
        tree = parse(source_code)
        p = Parser()
        for node in tree.body:
            if isinstance(node, (FunctionDef, ClassDef)):
>               p.api(root='my_project', node=node)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_api_0.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', node = <ast.FunctionDef object at 0x7fdb8eab82b0>

    def api(self, root: str, node: _API, *, prefix: str = '') -> None:
        """Create API doc for only functions and classes.
        Where `name` is the full name.
        """
        level = '#' * (self.b_level + (2 if not prefix else 3))
        name = _m(root, prefix, node.name)
>       self.level[name] = self.level[root]
E       KeyError: 'my_project'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:387: KeyError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        source_code = """
    def empty_func():
        pass
    """
        tree = parse(source_code)
        p = Parser(link=False, b_level=1, toc=True)
        node = tree.body[0]
    
>       p.api(root='my_project', node=node)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_api_0.py:70: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=True, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', node = <ast.FunctionDef object at 0x7fdb8eab8640>

    def api(self, root: str, node: _API, *, prefix: str = '') -> None:
        """Create API doc for only functions and classes.
        Where `name` is the full name.
        """
        level = '#' * (self.b_level + (2 if not prefix else 3))
        name = _m(root, prefix, node.name)
>       self.level[name] = self.level[root]
E       KeyError: 'my_project'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:387: KeyError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        source_code = """
    invalid_node = 42
    """
        tree = parse(source_code)
        p = Parser()
        node = tree.body[0]
    
        # This should not raise an exception and should simply do nothing
>       p.api(root='my_project', node=node)

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_api_0.py:85: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
root = 'my_project', node = <ast.Assign object at 0x7fdb8e9d6590>

    def api(self, root: str, node: _API, *, prefix: str = '') -> None:
        """Create API doc for only functions and classes.
        Where `name` is the full name.
        """
        level = '#' * (self.b_level + (2 if not prefix else 3))
>       name = _m(root, prefix, node.name)
E       AttributeError: 'Assign' object has no attribute 'name'

/opt/marta/baselines/codamosa/replication/test-apps/apimd/apimd/parser.py:386: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_api_0.py::test_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_api_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_Parser_api_0.py::test_invalid_inputs
============================== 3 failed in 0.10s ===============================
"""