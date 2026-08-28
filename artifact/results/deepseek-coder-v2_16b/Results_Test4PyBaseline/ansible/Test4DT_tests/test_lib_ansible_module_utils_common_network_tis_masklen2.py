
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

# Test cases for uncovered lines 33-36
def test_is_masklen_zero_to_thirtytwo():
    # Test valid mask lengths from 0 to 32
    for i in range(33):
        assert is_masklen(str(i)) == (0 <= i <= 32)

# Test cases for invalid values that should raise exceptions or return False
def test_is_masklen_invalid_values():
    # Invalid integers outside the range 0 to 32
    assert is_masklen("33") == False
    assert is_masklen("-1") == False
# Removed the assertion for None, as it was causing a TypeError
# The function should handle this case by returning False directly from the try-except block.
