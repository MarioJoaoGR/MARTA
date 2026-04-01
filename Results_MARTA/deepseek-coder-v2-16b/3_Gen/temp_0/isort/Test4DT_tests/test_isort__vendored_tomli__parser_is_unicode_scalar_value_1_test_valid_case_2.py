
import pytest

from isort._vendored.tomli._parser import is_unicode_scalar_value


def test_valid_case_2():
    # Test cases where codepoint should return True (valid Unicode scalar value)
    assert is_unicode_scalar_value(65)  # ASCII character 'A'
    assert is_unicode_scalar_value(1048575)  # Last possible code point in the range U+D7FF to U+E000
    
    # Test cases where codepoint should return False (invalid Unicode scalar value)
    assert not is_unicode_scalar_value(55296)  # First invalid code point after U+D7FF
    assert not is_unicode_scalar_value(1114112)  # Invalid code point above U+10FFFF
