
import pytest
import typing as T
from docstring_parser.numpydoc import _clean_str

# Test case for a non-empty string
def test_clean_str_non_empty():
    result = _clean_str("  Hello, World!  ")
    assert result == "Hello, World!"

# Test case for an empty string
def test_clean_str_empty():
    result = _clean_str("")
    assert result is None

# Test case for a string with only whitespace characters
def test_clean_str_whitespace():
    result = _clean_str("   ")