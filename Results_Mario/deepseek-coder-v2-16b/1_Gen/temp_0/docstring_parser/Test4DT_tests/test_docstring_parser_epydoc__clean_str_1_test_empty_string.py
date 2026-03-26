
import pytest
from docstring_parser import epydoc

def test_clean_str():
    # Test with a non-empty string
    assert epydoc._clean_str("  Hello, World!  ") == 'Hello, World!'
    
    # Test with an empty string
    assert epydoc._clean_str("") is None
    
    # Test with a whitespace string
    assert epydoc._clean_str("   ") is None
