
import pytest
from docstring_parser.rest import parse, Docstring, DocstringStyle, DocstringParam, DocstringReturns
import typing as T

def test_none_input():
    text = None
    result = parse(text)
    assert isinstance(result, Docstring), "Expected a Docstring object"
    assert result.short_description is None, "Expected short description to be None for null input"
    assert result.long_description is None, "Expected long description to be None for null input"
