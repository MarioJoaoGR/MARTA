
import pytest
from docstring_parser.numpydoc import _clean_str

def test_whitespace_only():
    assert _clean_str("  Hello, World!  ") == "Hello, World!"
    assert _clean_str("") is None
    assert _clean_str("   ") is None
