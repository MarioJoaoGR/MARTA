
import ast
import pytest
from docstring_parser.attrdoc import AttributeDocstrings

class TestAttributeDocstrings:
    def test_valid_input(self):
        # Define a sample module with attribute definitions
        code = """
        class SampleClass:
            attr1: int = 10
            attr2: str = 'hello'
        """
        tree = ast.parse(code)
    
        visitor = AttributeDocstrings()
        for stmt in tree.body:
            visitor.visit(stmt)
    
        assert visitor.attr_docs == {
            'attr1': ('int', 10),
            'attr2': ('str', 'hello')
        }

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
___________________ TestAttributeDocstrings.test_valid_input ___________________

self = <Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_input.TestAttributeDocstrings object at 0x1066c2aa0>

    def test_valid_input(self):
        # Define a sample module with attribute definitions
        code = """
        class SampleClass:
            attr1: int = 10
            attr2: str = 'hello'
        """
>       tree = ast.parse(code)

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_input.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = "\n        class SampleClass:\n            attr1: int = 10\n            attr2: str = 'hello'\n        "
filename = '<unknown>', mode = 'exec'

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
E           class SampleClass:
E       IndentationError: unexpected indent

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/ast.py:50: IndentationError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_visit_0_test_valid_input.py::TestAttributeDocstrings::test_valid_input
============================== 1 failed in 0.04s ===============================
"""