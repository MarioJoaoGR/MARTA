
import ast
from typing import Optional as T
import pytest

# Assuming the function is defined in a module named docstring_parser.attrdoc
from docstring_parser.attrdoc import ast_get_attribute

def test_ast_get_attribute_with_assign():
    # Create an AST node for assignment
    assign_node = ast.parse("x = y").body[0]
    result = ast_get_attribute(assign_node)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_ast_get_attribute_with_assign ______________________

    def test_ast_get_attribute_with_assign():
        # Create an AST node for assignment
        assign_node = ast.parse("x = y").body[0]
        result = ast_get_attribute(assign_node)
>       assert result == ('y', None, 'y')
E       AssertionError: assert ('x', None, 'y') == ('y', None, 'y')
E         
E         At index 0 diff: 'x' != 'y'
E         Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_attribute_0.py::test_ast_get_attribute_with_assign
========================= 1 failed, 1 passed in 0.02s ==========================

"""