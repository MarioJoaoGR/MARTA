
import ast
import typing as T
from docstring_parser.attrdoc import ast_get_attribute, ast_unparse

def test_invalid_node_type():
    # Create an invalid node type to trigger the error in the function
    class InvalidNode(ast.AST):
        pass
    
    invalid_node = InvalidNode()
    
    # Call the function and check if it returns None as expected for an invalid node type
    result = ast_get_attribute(invalid_node)
    assert result is None, "Expected None for an invalid node type"
