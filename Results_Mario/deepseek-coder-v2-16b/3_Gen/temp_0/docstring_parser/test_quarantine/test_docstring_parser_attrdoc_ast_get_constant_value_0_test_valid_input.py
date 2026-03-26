
import ast
from typing import Any as T
import pytest
from docstring_parser.attrdoc import ast_get_constant_value

@pytest.fixture
def example_node():
    # Create an AST node representing a constant expression
    return ast.parse("1 + 2").body[0].value

def test_valid_input(example_node):
    assert ast_get_constant_value(example_node) == 3

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

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_constant_value_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

example_node = <ast.BinOp object at 0x103a30370>

    def test_valid_input(example_node):
>       assert ast_get_constant_value(example_node) == 3

docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_constant_value_0_test_valid_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = <ast.BinOp object at 0x103a30370>

    def ast_get_constant_value(node: ast.AST) -> T.Any:
        """Return the constant's value if the given node is a constant."""
>       return getattr(node, "value")
E       AttributeError: 'BinOp' object has no attribute 'value'

docstring_parser/docstring_parser/attrdoc.py:17: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_constant_value_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""