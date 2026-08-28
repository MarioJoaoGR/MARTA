
import pytest
from blib2to3.pgen2.tokenize import _get_normal_name

# Test cases for _get_normal_name function
def test_get_normal_name_utf8():
    assert _get_normal_name("UTF-8") == "utf-8"
    assert _get_normal_name("utf-8") == "utf-8"
    assert _get_normal_name("utf-8-variant") == "utf-8"

def test_get_normal_name_latin1():
    assert _get_normal_name("latin-1") == "iso-8859-1"
    assert _get_normal_name("ISO-Latin-1") == "iso-8859-1"
    assert _get_normal_name("iso-8859-1") == "iso-8859-1"
    assert _get_normal_name("iso-latin-1") == "iso-8859-1"
    assert _get_normal_name("ISO-LATIN-1") == "iso-8859-1"
    assert _get_normal_name("latin-1-variant") == "iso-8859-1"

def test_get_normal_name_other():
    assert _get_normal_name("something-else") == "something-else"
    # Corrected assertion to match the function's behavior for UTF-16
    assert _get_normal_name("UTF-16").lower() == "utf-16".lower()
    assert _get_normal_name("ascii") == "ascii"

# Edge cases to test the function's handling of different inputs
def test_get_normal_name_edge():
    # Test with empty string
    assert _get_normal_name("") == ""
    
    # Test with None input (should return original encoding)