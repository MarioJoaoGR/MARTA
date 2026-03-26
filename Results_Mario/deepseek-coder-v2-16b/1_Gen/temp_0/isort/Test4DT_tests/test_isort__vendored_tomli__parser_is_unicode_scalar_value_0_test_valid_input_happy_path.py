
from isort._vendored.tomli._parser import is_unicode_scalar_value

def test_valid_input_happy_path():
    # Test cases for valid Unicode scalar values
    assert is_unicode_scalar_value(65)  # ASCII character 'A'
    assert is_unicode_scalar_value(1048575)  # Last possible code point in the range U+D7FF to U+E000
    
    # Test cases for invalid Unicode scalar values
    assert not is_unicode_scalar_value(55296)  # First invalid code point after U+D7FF
    assert not is_unicode_scalar_value(1114112)  # Invalid code point above U+10FFFF
