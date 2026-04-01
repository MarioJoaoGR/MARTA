
import ast
import pytest

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(ast_get_constant_value(node.value), str)
    )

def test_invalid_type():
    # Create an AST node with a non-literal type (e.g., int)
    node = ast.Expr(value=ast.Constant(value=42))
    
    # Test the function with the invalid node
    assert not ast_is_literal_str(node), "Expected False for an AST node of invalid type"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_ast_is_literal_str_0_test_invalid_type
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0_test_invalid_type.py:10:23: E0602: Undefined variable 'ast_get_constant_value' (undefined-variable)


"""