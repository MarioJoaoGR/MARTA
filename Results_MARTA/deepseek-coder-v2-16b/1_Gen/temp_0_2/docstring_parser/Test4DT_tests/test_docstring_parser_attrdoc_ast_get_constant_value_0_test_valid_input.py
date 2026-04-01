
import ast
import pytest
import typing as T

def ast_get_constant_value(node: ast.AST) -> T.Any:
    """Return the constant's value if the given node is a constant."""
    return getattr(node, "value", None)

@pytest.fixture
def valid_const_node():
    return ast.Constant(value=42)

def test_valid_input(valid_const_node):
    result = ast_get_constant_value(valid_const_node)
    assert result == 42
