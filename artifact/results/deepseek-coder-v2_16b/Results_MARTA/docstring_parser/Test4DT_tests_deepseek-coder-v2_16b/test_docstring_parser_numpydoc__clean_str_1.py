
import pytest
import typing as T
from docstring_parser.numpydoc import _clean_str


def test_empty_string():
    result = _clean_str("")
    assert result is None, f"Expected None for empty string, but got {result}"

def test_whitespace_only():
    result = _clean_str("   ")
    assert result is None, f"Expected None for whitespace-only string, but got {result}"

def test_string_with_content():
    result = _clean_str("  Hello, World!  ")
    assert result == "Hello, World!", f"Expected 'Hello, World!' for input with content, but got {result}"