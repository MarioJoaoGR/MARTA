
import ast
import pytest
from docstring_parser.attrdoc import ast_is_literal_str, ast_get_constant_value

def test_invalid_type():
    # Create a mock AST node that does not represent a literal string
    invalid_node = ast.Expr(value=ast.Constant(value=42))  # Integer instead of string
    
    # Check if the function correctly identifies an invalid type
    assert not ast_is_literal_str(invalid_node), "Expected False for non-string literal"
