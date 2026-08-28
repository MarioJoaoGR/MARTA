
import pytest
from docstring_parser.numpydoc import _clean_str
import typing as T

def test_clean_str_with_leading_and_trailing_whitespace():
    result = _clean_str("  hello world  ")
    assert result == "hello world"

def test_clean_str_with_only_whitespace():
    result = _clean_str("   ")
    assert result is None

def test_clean_str_with_empty_string():
    result = _clean_str("")
    assert result is None

def test_clean_str_with_no_whitespace():
    result = _clean_str("python")
    assert result == "python"

