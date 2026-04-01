
import ast
from docstring_parser import attrdoc

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )

# Test case for None input scenario
def test_none_input():
    """Test that the function correctly handles a None input."""
    assert not ast_is_literal_str(None), "Expected False for None input"
