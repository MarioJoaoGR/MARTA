
import ast
import pytest
from docstring_parser.attrdoc import ast_get_attribute

def test_invalid_input():
    # Setup: Create an invalid AST node (e.g., a simple Name node)
    example_node = ast.parse('print(1)').body[0].value  # This is a Name node, not Assign or AnnAssign
    
    # Function call with the invalid node
    result = ast_get_attribute(example_node)
    
    # Expected output: Should return None since it's an invalid input type
    assert result is None
