
import ast
import pytest

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(ast_get_constant_value(node.value), str)
    )

def test_ast_is_literal_str():
    # Test a literal string AST node
    expr_node = ast.Expr(value=ast.Constant(value="Hello, World!"))
    assert ast_is_literal_str(expr_node) is True

    # Test an integer AST node
    int_node = ast.Expr(value=ast.Constant(value=42))
    assert ast_is_literal_str(int_node) is False

    # Test a float AST node
    float_node = ast.Expr(value=ast.Constant(value=3.14))
    assert ast_is_literal_str(float_node) is False

    # Test a boolean AST node
    bool_node = ast.Expr(value=ast.Constant(value=True))
    assert ast_is_literal_str(bool_node) is False

    print("All tests passed!")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_ast_is_literal_str_0_test_valid_literal_string
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0_test_valid_literal_string.py:10:23: E0602: Undefined variable 'ast_get_constant_value' (undefined-variable)


"""