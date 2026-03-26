
import ast
from unittest import mock

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )

def test_invalid_input():
    # Create an invalid AST node for testing
    class InvalidASTNode:
        pass
    
    invalid_node = InvalidASTNode()
    
    assert not ast_is_literal_str(invalid_node), "Expected False for invalid input"
