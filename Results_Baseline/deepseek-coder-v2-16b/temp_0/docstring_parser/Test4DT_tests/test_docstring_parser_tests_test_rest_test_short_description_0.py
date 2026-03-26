
import pytest
from docstring_parser import parse
import typing as T

# Test cases for the test_short_description function
def test_short_description_with_source():
    source = "This is a brief description."
    expected = "This is a brief description."
    docstring = parse(source)
    assert docstring.short_description == expected, f"Expected short description: {expected}, but got: {docstring.short_description}"
    assert docstring.description == expected, f"Expected description: {expected}, but got: {docstring.description}"
    assert docstring.long_description is None, "Expected long description to be None"
    assert not docstring.meta, "Expected meta to be empty"

def test_short_description_without_source():
    source = None
    expected = None
    docstring = parse(source)
    assert docstring.short_description == expected, f"Expected short description: {expected}, but got: {docstring.short_description}"
    assert docstring.description == expected, f"Expected description: {expected}, but got: {docstring.description}"
    assert docstring.long_description is None, "Expected long description to be None"
    assert not docstring.meta, "Expected meta to be empty"

def test_short_description_with_empty_source():
    source = ""
    expected = ""
    docstring = parse(source)