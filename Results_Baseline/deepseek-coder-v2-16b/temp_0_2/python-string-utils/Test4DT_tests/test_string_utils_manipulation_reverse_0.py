# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import reverse
from string_utils.errors import InvalidInputError

# Test cases for the reverse function
def test_reverse_valid_string():
    assert reverse('hello') == 'olleh'
    assert reverse('Python') == 'nohtyP'

def test_reverse_invalid_input():
    with pytest.raises(InvalidInputError):
        reverse(12345)  # This should raise InvalidInputError since the argument is not a string

# Additional test cases to cover edge cases and potential issues
def test_reverse_empty_string():
    assert reverse('') == ''

def test_reverse_single_character():
    assert reverse('a') == 'a'

def test_reverse_none_input():
    with pytest.raises(InvalidInputError):
        reverse(None)  # This should raise InvalidInputError since None is not a string
