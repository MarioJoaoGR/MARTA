
import pytest
from string_utils.manipulation import reverse, InvalidInputError

def test_reverse_basic():
    # Test basic functionality with a simple string
    assert reverse('hello') == 'olleh'
    
    # Test with an empty string
    assert reverse('') == ''
    
    # Test with a string containing numbers and special characters
    assert reverse('Python3.8') == '8.3nohtyP'

def test_reverse_invalid_input():
    # Test with an invalid input type (integer)
    with pytest.raises(InvalidInputError) as excinfo:
        reverse(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

    # Test with another invalid input type (list)
    with pytest.raises(InvalidInputError) as excinfo:
        reverse(['a', 'b', 'c'])
    assert str(excinfo.value) == 'Expected "str", received "list"'
