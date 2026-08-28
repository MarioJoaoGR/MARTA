
import pytest
from unittest.mock import patch
from string_utils.manipulation import InvalidInputError, is_string

def reverse(input_string: str) -> str:
    """
    Returns the string with its chars reversed.

    *Example:*

    >>> reverse('hello') # returns 'olleh'

    :param input_string: String to revert.
    :type input_string: str
    :return: Reversed string.
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    return input_string[::-1]

# Test scenarios
def test_valid_input():
    with patch('string_utils.manipulation.is_string', return_value=True):
        assert reverse('hello') == 'olleh'

def test_edge_case():
    # None input
    with patch('string_utils.manipulation.is_string', side_effect=[False, True]):
        with pytest.raises(InvalidInputError):
            reverse(None)
    
    # Empty string
    with patch('string_utils.manipulation.is_string', return_value=True):
        assert reverse('') == ''
    
    # Very long string (mocking is_string to always return True for demonstration purposes)
    very_long_string = 'a' * 1000000  # Creating a very long string
    with patch('string_utils.manipulation.is_string', return_value=True):
        assert reverse(very_long_string) == very_long_string[::-1]

def test_invalid_input():
    with patch('string_utils.manipulation.is_string', side_effect=[False, True]):
        with pytest.raises(InvalidInputError):
            reverse(12345)
