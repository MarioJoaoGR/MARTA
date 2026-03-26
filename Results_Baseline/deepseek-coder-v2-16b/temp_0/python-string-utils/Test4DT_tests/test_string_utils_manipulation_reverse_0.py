# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import reverse
from string_utils.errors import InvalidInputError

# Test cases for the reverse function
def test_reverse_valid_string():
    assert reverse('hello') == 'olleh'
    assert reverse('world') == 'dlrow'

def test_reverse_invalid_input():
    with pytest.raises(InvalidInputError):
        reverse(123)

# Additional edge cases can be added to cover more scenarios
def test_reverse_empty_string():
    assert reverse('') == ''

def test_reverse_single_character_string():
    assert reverse('a') == 'a'

def test_reverse_palindrome():
    assert reverse('madam') == 'madam'  # This should pass since the function does not check for palindromes
