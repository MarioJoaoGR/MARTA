
import pytest
from docstring_parser.epydoc import parse, Docstring, ParseError
import typing as T

def test_none_input():
    # Test when text is None
    result = parse(None)
    assert isinstance(result, Docstring), "Expected a Docstring object"
    assert result.short_description is None, "Expected short description to be None"
    assert len(result.meta) == 0, "Expected no metadata"
