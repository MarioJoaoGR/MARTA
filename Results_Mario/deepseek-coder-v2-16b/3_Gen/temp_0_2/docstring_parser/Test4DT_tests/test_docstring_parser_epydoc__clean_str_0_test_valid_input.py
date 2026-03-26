
import pytest
from typing import Optional, T  # Ensure we have a correct import for Optional
from docstring_parser.epydoc import _clean_str  # Import the function from its module

def test_valid_input():
    assert _clean_str("  Hello, World!  ") == 'Hello, World!'
    assert _clean_str("") is None
    assert _clean_str("   ") is None
