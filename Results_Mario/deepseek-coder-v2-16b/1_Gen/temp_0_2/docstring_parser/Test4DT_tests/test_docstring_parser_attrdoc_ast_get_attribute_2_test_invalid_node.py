
import ast
import typing as T
from docstring_parser import attrdoc

def test_invalid_node():
    # Create an invalid AST node by parsing a simple expression
    invalid_node = ast.parse('1 + 2')
    
    # Call the function with the invalid node
    result = attrdoc.ast_get_attribute(invalid_node)
    
    # Assert that the result is None for an invalid node type
    assert result is None
