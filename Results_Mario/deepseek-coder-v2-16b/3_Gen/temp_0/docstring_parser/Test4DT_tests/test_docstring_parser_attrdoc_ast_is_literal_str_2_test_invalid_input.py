
import ast
from docstring_parser import attrdoc

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )

def test_invalid_input():
    # Test case for invalid input where node is not an AST expression
    class InvalidNode:
        pass
    
    invalid_node = InvalidNode()
    assert not ast_is_literal_str(invalid_node), "Expected False for invalid node type"

    # Additional test cases can be added here to cover different scenarios of invalid input.
