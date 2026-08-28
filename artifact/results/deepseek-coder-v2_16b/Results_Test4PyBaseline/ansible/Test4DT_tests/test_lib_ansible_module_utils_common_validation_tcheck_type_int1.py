
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

# Additional test cases for uncovered lines
def test_check_type_int_none():
    """Test that passing None raises a TypeError."""
    with pytest.raises(TypeError) as excinfo:
        check_type_int(None)

def test_check_type_int_float():
    """Test that a float is not accepted and raises a TypeError."""
    with pytest.raises(TypeError) as excinfo:
        check_type_int(123.45)

def test_check_type_int_list():
    """Test that passing a list raises a TypeError."""
    with pytest.raises(TypeError) as excinfo:
        check_type_int([1, 2, 3])

def test_check_type_int_dict():
    """Test that passing a dictionary raises a TypeError."""
    with pytest.raises(TypeError) as excinfo:
        check_type_int({'a': 1})

def test_check_type_int_set():
    """Test that passing a set raises a TypeError."""
    with pytest.raises(TypeError) as excinfo:
        check_type_int({1, 2, 3})
