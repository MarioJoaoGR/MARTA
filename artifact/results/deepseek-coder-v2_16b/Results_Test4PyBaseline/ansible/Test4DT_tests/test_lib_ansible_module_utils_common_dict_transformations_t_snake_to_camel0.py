
import pytest
from ansible.module_utils.common.dict_transformations import _snake_to_camel

# Test cases for _snake_to_camel function

def test_basic_conversion():
    assert _snake_to_camel('this_is_a_test') == 'thisIsATest'

def test_capitalization():
    assert _snake_to_camel('this_is_a_test', capitalize_first=True) == 'ThisIsATest'

def test_another_example():
    assert _snake_to_camel('another_example') == 'anotherExample'

# Additional edge cases to consider:

def test_empty_string():
    assert _snake_to_camel('') == ''

def test_no_underscores():
    assert _snake_to_camel('uppercase') == 'uppercase'

def test_single_word():
    assert _snake_to_camel('singleword') == 'singleword'

# Test cases for the function when `capitalize_first` is False by default:

def test_default_capitalization():
    assert _snake_to_camel('another_example', capitalize_first=False) == 'anotherExample'

# Test cases to ensure proper handling of different input scenarios:

def test_mixed_case_input():
    with pytest.raises(TypeError):  # Assuming the function should raise a TypeError if non-string inputs are provided
        _snake_to_camel(12345)

def test_non_string_input():
    with pytest.raises(TypeError):
        _snake_to_camel(None)

# Test cases to ensure the function handles edge cases correctly:

def test_long_snake_case():
    assert _snake_to_camel('this_is_a_very_long_test') == 'thisIsAVeryLongTest'

if __name__ == '__main__':
    pytest.main()
