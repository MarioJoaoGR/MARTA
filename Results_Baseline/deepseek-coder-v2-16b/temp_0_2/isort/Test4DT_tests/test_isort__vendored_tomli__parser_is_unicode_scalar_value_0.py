# Module: isort._vendored.tomli._parser
import pytest

from isort._vendored.tomli._parser import is_unicode_scalar_value


# Test cases for the function `is_unicode_scalar_value`
def test_valid_ascii():
    assert is_unicode_scalar_value(65) == True, "Expected True for ASCII character 'A' (codepoint 65)"

def test_valid_high_surrogate():
    assert is_unicode_scalar_value(1048575) == True, "Expected True for the last possible code point in the range U+D7FF to U+E000"

def test_invalid_low_surrogate():
    assert is_unicode_scalar_value(55296) == False, "Expected False for the first invalid code point after valid range"

def test_invalid_beyond_range():
    assert is_unicode_scalar_value(1114112) == False, "Expected False for a code point one past the last possible code point"

# Run the tests when this script is executed
if __name__ == "__main__":
    pytest.main()
