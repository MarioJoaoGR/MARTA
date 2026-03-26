
import pytest
from docstring_parser.numpydoc import parse
from docstring_parser.numpydoc import Docstring
import typing as T

def test_none_input():
    # Test when no input is provided
    parsed_docstring = parse(None)
    assert isinstance(parsed_docstring, Docstring), "Expected a Docstring object"
