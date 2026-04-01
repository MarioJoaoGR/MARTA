
import pytest
from docstring_parser.epydoc import parse, Docstring, ParseError
import typing as T

@pytest.mark.parametrize("input_text", [None])
def test_none_input(input_text):
    result = parse(input_text)
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert len(result.meta) == 0
