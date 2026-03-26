
import ast
import pytest

def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(ast_get_constant_value(node.value), str)
    )

def test_invalid_input():
    # Create an invalid AST node by using a different type of expression
    example_node = ast.parse('123').body[0].value  # This is an ast.Num, not an ast.Expr or ast.Constant
    
    assert not ast_is_literal_str(example_node), "Expected False for invalid AST node type"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_ast_is_literal_str_0_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_0_test_invalid_input.py:10:23: E0602: Undefined variable 'ast_get_constant_value' (undefined-variable)


"""