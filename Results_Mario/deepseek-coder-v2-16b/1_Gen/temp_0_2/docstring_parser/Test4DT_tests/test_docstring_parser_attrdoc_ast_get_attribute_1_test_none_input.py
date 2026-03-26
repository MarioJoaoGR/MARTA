
import ast
from docstring_parser.attrdoc import ast_get_attribute
import typing as T

def test_none_input():
    # Test when input node is None
    result = ast_get_attribute(None)
    assert result is None, f"Expected None but got {result}"
