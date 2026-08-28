
# Module: ansible.module_utils.common.validation
from ansible.module_utils.common.validation import check_type_int
import pytest

# Test cases for check_type_int function
def test_check_type_int_integer():
    """Test that an integer value is returned as it is."""
    assert check_type_int(123) == 123

def test_check_type_int_string_convertible():
    """Test that a string representing an integer is converted to an integer."""
    assert check_type_int('456') == 456

def test_check_type_int_string_not_convertible():
    """Test that a string not representing an integer raises a TypeError."""
    with pytest.raises(TypeError) as excinfo:
        check_type_int('abc')