
import ast
from docstring_parser.attrdoc import ast_unparse
import pytest

def test_valid_input_name_node():
    # Create an AST Name node with id 'x'
    name_node = ast.Name(id='x')
    
    # Call the function under test
    result = ast_unparse(name_node)
    
    # Assert that the result is the string representation of the name node
    assert result == 'x'
