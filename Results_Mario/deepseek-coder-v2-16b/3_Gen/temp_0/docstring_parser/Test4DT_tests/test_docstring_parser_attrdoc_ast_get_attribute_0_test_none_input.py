
import ast
from docstring_parser.attrdoc import ast_get_attribute
import typing as T
import pytest

@pytest.mark.parametrize("node", [
    None,  # Test with None input
])
def test_none_input(node):
    result = ast_get_attribute(node)
    assert result is None
