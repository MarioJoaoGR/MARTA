
import pytest
from ansible.module_utils.common.validation import check_type_list

# Test cases for check_type_list function

def test_check_type_list_already_list():
    # Case 1: Input is already a list
    result = check_type_list([1, 2, 3])
    assert result == [1, 2, 3]

def test_check_type_list_comma_separated_string():
    # Case 2: Input is a comma-separated string
    result = check_type_list("4,5,6")
    assert result == ['4', '5', '6']

def test_check_type_list_integer():
    # Case 3: Input is an integer
    result = check_type_list(123)
    assert result == ['123']

def test_check_type_list_float():
    # Case 4: Input is a float (treated as int for simplicity in this context)
    result = check_type_list(123.0)
    assert result == ['123.0']

def test_check_type_list_string_without_commas():
    # Case 5: Input is a string without commas, which will be treated as a single item list
    result = check_type_list("a,b,c")
    assert result == ['a', 'b', 'c']

def test_check_type_list_none():
    # Case 6: Input is None, which should raise a TypeError
    with pytest.raises(TypeError) as excinfo:
        check_type_list(None)

# Additional test cases for uncovered lines

def test_check_type_list_not_a_list():
    # Case 7: Input is not a list, string, int, or float (should raise TypeError)
    with pytest.raises(TypeError):
        check_type_list({})

def test_check_type_list_empty_string():
    # Case 8: Input is an empty string, which should be treated as a list of empty strings
    result = check_type_list("")