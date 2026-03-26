
import ast
from docstring_parser.attrdoc import ast_get_attribute

def test_valid_input():
    """
    Test the `ast_get_attribute` function with a valid AST node representing an attribute assignment.
    """
    # Example AST node for an attribute assignment
    assign_node = ast.Assign(targets=[ast.Name(id='x')], value=ast.Constant(value=42))
    
    # Get the attribute details
    attr_info = ast_get_attribute(assign_node)
    assert attr_info == ('x', None, '42')
