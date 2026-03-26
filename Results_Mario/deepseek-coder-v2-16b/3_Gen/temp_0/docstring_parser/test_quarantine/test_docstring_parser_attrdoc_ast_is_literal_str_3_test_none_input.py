
import ast
from unittest.mock import patch, MagicMock
import pytest

# Assuming the function is defined as shown above
def ast_is_literal_str(node: ast.AST) -> bool:
    """Return True if the given node is a literal string."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(ast_get_constant_value(node.value), str)
    )

# Mocking the necessary parts of the ast module
@patch('ast.AST')
@patch('ast.Expr')
@patch('ast.Constant')
def test_ast_is_literal_str(MockConstant, MockExpr, MockAST):
    # Create a mock for the node value
    mock_value = MagicMock()
    mock_constant = MagicMock()
    
    # Set up the mocks to return each other when isinstance checks are done
    MockExpr.return_value = mock_value
    MockConstant.return_value = mock_constant
    mock_value.value = mock_constant
    
    # Test case where node is a literal string
    assert ast_is_literal_str(MockAST()) == True

    # Test case where node is not a literal string (e.g., an integer)
    mock_constant.return_value = 123
    assert ast_is_literal_str(MockAST()) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_ast_is_literal_str_3_test_none_input
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_ast_is_literal_str_3_test_none_input.py:12:23: E0602: Undefined variable 'ast_get_constant_value' (undefined-variable)


"""