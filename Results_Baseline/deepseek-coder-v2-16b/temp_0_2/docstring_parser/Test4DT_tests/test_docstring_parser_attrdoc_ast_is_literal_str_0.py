
import ast
from docstring_parser.attrdoc import ast_is_literal_str

def test_ast_is_literal_str_with_literal_string():
    example_node = ast.parse("'Hello, World!'").body[0]
    assert ast_is_literal_str(example_node) is True

def test_ast_is_literal_str_with_non_literal_string():
    example_node = ast.parse("1 + 2").body[0].value
    assert ast_is_literal_str(example_node) is False

def test_ast_is_literal_str_with_assignment_containing_literal_string():
    example_node = ast.parse("x = 'Hello, World!'").body[0].value