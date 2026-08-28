# Module: docstring_parser.numpydoc
import pytest
from docstring_parser.numpydoc import _clean_str

def test_clean_str_with_leading_and_trailing_whitespace():
    assert _clean_str("   hello world   ") == "hello world"

def test_clean_str_with_only_whitespace():
    assert _clean_str("   ") is None

def test_clean_str_with_empty_string():
    assert _clean_str("") is None

def test_clean_str_without_whitespace():
    assert _clean_str("hello world") == "hello world"

def test_clean_str_with_mixed_case_and_whitespace():
    assert _clean_str("  Hello World  ") == "Hello World"

def test_clean_str_with_special_characters():
    assert _clean_str("   @#$$%^&*()   ") == "@#$$%^&*()"
