# Module: docstring_parser.numpydoc
import pytest
import typing as T
from docstring_parser.numpydoc import _clean_str

# Test case for a string with leading and trailing whitespace
def test_clean_str_with_whitespace():
    result = _clean_str("  Hello, World!  ")
    assert result == "Hello, World!"

# Test case for an empty string
def test_clean_str_empty_string():
    result = _clean_str("")
    assert result is None

# Test case for a string with only whitespace characters
def test_clean_str_only_whitespace():
    result = _clean_str("   ")
    assert result is None
