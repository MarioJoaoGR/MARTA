
import ast
import pytest
from docstring_parser import attrdoc

def test_valid_constant_node():
    # Create an AST constant node with a value of 42
    const_node = ast.Constant(value=42)
    
    # Call the function under test
    result = attrdoc.ast_unparse(const_node)
    
    # Check if the result is as expected
    assert result == '42'
