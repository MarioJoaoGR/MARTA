
import pytest
from isort._vendored.tomli._parser import is_unicode_scalar_value

def test_edge_cases():
    # Test cases for Unicode scalar values
    assert is_unicode_scalar_value(65)  # ASCII 'A'
    assert is_unicode_scalar_value(1048575)  # U+FFFFF
    assert not is_unicode_scalar_value(-5)  # Negative value
    assert not is_unicode_scalar_value(1114112)  # Out of range (U+10FFFF + 1)
