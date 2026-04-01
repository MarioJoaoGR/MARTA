
import ast
from docstring_parser.attrdoc import ast_is_literal_str

def test_ast_is_literal_str_with_none():
    # Test when node is None
    assert not ast_is_literal_str(None), "Expected False for None input"
