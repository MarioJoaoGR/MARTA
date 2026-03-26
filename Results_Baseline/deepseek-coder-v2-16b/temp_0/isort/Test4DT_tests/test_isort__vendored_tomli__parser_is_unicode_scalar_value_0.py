
import pytest

from isort._vendored.tomli._parser import is_unicode_scalar_value


# Test cases for the function `is_unicode_scalar_value`
def test_valid_codepoints():
    # ASCII character 'A' (codepoint 65) is within the valid range
    assert is_unicode_scalar_value(65) == True
    
    # Last possible code point in the range U+D7FF to U+E000 (codepoint 1048575) is within the valid range
    assert is_unicode_scalar_value(1048575) == True

def test_invalid_codepoints():
    # First invalid code point after U+D7FF (codepoint 55296) is not within the valid range
    assert is_unicode_scalar_value(55296) == False
    
    # Invalid code point above U+10FFFF (codepoint 1114112) is not within the valid range
    assert is_unicode_scalar_value(1114112) == False

# Additional test cases to cover edge cases and potential failure points
def test_edge_cases():
    # Minimum valid codepoint (0) should return True
    assert is_unicode_scalar_value(0) == True
    
    # Maximum valid codepoint within the first range (55295) should return True
    assert is_unicode_scalar_value(55295) == True
    
    # Minimum invalid codepoint after U+D7FF (55296) should return False
    assert is_unicode_scalar_value(55296) == False
    
    # Maximum valid codepoint within the second range (1114111) should return True
    assert is_unicode_scalar_value(1114111) == True
    
    # Codepoint above U+10FFFF (1114112) should return False