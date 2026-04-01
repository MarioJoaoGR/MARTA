
import ast
import pytest
from unittest.mock import patch

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(ast_get_constant_value(node.value), str)
    )

@pytest.mark.parametrize("invalid_node", [
    pytest.param(None, id="NoneType"),
    pytest.param([], id="List"),
    pytest.param({}, id="Dict"),
    pytest.param(123, id="Int"),
    pytest.param(b'bytes', id="Bytes"),
])
def test_invalid_input(invalid_node):
    with pytest.raises(AttributeError):
        ast_is_literal_str(invalid_node)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_ast_is_literal_str_2_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_2_test_invalid_input.py:11:23: E0602: Undefined variable 'ast_get_constant_value' (undefined-variable)


"""