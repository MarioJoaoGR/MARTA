
import ast
import pytest
from docstring_parser import attrdoc

def test_valid_name_node():
    # Create an AST Name node with a valid identifier
    name_node = ast.Name(id='example_identifier', ctx=ast.Load())
    
    # Call the function under test
    result = attrdoc.ast_unparse(name_node)
    
    # Check if the result matches the expected output
    assert result == 'example_identifier'
