
import pytest
import typing as T  # Importing 'T' for type annotations
from docstring_parser.epydoc import _clean_str  # Assuming this is the correct module path

def test_whitespace_only():
    assert _clean_str("  Hello, World!  ") == "Hello, World!"
    assert _clean_str("") is None
    assert _clean_str("   ") is None
