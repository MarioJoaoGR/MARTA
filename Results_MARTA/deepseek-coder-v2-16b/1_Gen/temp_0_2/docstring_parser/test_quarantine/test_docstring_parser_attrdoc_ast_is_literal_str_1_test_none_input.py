
import ast
import pytest

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(ast_get_constant_value(node.value), str)
    )

# Test case for ast_is_literal_str function
def test_ast_is_literal_str():
    # Create an AST node representing a literal string
    expr_node = ast.Expr(value=ast.Constant(value="Hello, World!"))
    
    # Check if the node is identified as a literal string
    assert ast_is_literal_str(expr_node) == True

    # Create an AST node representing a non-string literal
    expr_node = ast.Expr(value=ast.Constant(value=42))
    
    # Check if the node is identified as not a literal string
    assert ast_is_literal_str(expr_node) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_ast_is_literal_str_1_test_none_input
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_1_test_none_input.py:10:23: E0602: Undefined variable 'ast_get_constant_value' (undefined-variable)


"""