
import pytest
from ansible.module_utils.common.network import is_masklen

# Test cases for valid netmask lengths
def test_is_masklen_valid():
    assert is_masklen("24") == True
    assert is_masklen("32") == True
    assert is_masklen("16") == True
    assert is_masklen("0") == True

# Test cases for invalid netmask lengths
def test_is_masklen_invalid():
    assert is_masklen("-1") == False
    assert is_masklen("33") == False
    assert is_masklen("abc") == False

# Additional test case to check the function's behavior with non-integer strings
def test_is_masklen_non_integer():
    assert is_masklen("abc") == False

# Test case for invalid input type (None)
def test_is_masklen_invalid_type():
    with pytest.raises(TypeError):
        is_masklen(None)

# Test case for valid input as float (should be converted to int and checked)
def test_is_masklen_valid_float():
    assert is_masklen("24.0") == False

# Test case for empty string input
def test_is_masklen_empty_string():
    assert is_masklen("") == False
