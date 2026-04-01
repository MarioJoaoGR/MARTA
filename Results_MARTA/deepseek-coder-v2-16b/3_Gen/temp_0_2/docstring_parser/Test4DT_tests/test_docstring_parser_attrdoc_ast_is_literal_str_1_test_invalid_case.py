
import ast
from docstring_parser.attrdoc import ast_is_literal_str

def test_invalid_case():
    # Create a mock AST node that is not a literal string
    class MockNode:
        def __init__(self):
            self.value = None
    
    mock_node = MockNode()
    mock_node.value = ast.Constant(value="not a string")
    
    # Call the function with the invalid node
    result = ast_is_literal_str(mock_node)
    
    # Assert that the result is False since it's not a literal string
    assert not result, "Expected False for an invalid AST node representing a non-string literal"
