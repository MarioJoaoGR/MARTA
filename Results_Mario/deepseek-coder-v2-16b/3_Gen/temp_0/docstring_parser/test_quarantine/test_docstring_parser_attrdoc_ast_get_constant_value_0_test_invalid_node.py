
import ast
from typing import Any as T
import pytest

def ast_get_constant_value(node: ast.AST) -> T.Any:
    """Return the constant's value if the given node is a constant."""
    return getattr(node, "value", None)

# Test case for invalid node type
def test_invalid_node():
    # Create an AST node that is not a constant (e.g., an expression node)
    example_node = ast.parse("1 + 2").body[0]  # This represents an expression, not a constant
    
    # Call the function with the invalid node and check if it returns None
    result = ast_get_constant_value(example_node)
    assert result is None, f"Expected None for non-constant node, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_docstring_parser_attrdoc_ast_get_constant_value_0_test_invalid_node.py _
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_constant_value_0_test_invalid_node.py:6: in <module>
    def ast_get_constant_value(node: ast.AST) -> T.Any:
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/typing.py:375: in __getattr__
    raise AttributeError(item)
E   AttributeError: Any
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_get_constant_value_0_test_invalid_node.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""