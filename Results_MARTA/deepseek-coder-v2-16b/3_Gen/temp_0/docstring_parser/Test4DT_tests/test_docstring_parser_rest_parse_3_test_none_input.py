
import pytest
from docstring_parser.rest import Docstring, parse
import typing as T

def test_none_input():
    text = None
    result = parse(text)
    assert isinstance(result, Docstring), "Expected a Docstring instance"
    assert not result.short_description, "Expected short description to be empty"
    assert not result.long_description, "Expected long description to be empty"
    assert not result.meta, "Expected metadata to be empty"
