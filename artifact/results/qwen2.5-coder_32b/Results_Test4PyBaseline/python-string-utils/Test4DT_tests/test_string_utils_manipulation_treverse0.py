# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import reverse, InvalidInputError

def test_reverse_with_valid_strings():
    assert reverse('hello') == 'olleh'
    assert reverse('') == ''
    assert reverse('Python3.8') == '8.3nohtyP'
    assert reverse('a') == 'a'
    assert reverse('12345') == '54321'

def test_reverse_with_non_string_input():
    with pytest.raises(InvalidInputError) as excinfo:
        reverse(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

    with pytest.raises(InvalidInputError) as excinfo:
        reverse([1, 2, 3])
    assert str(excinfo.value) == 'Expected "str", received "list"'

    with pytest.raises(InvalidInputError) as excinfo:
        reverse({'key': 'value'})
    assert str(excinfo.value) == 'Expected "str", received "dict"'

def test_reverse_with_none_input():
    with pytest.raises(InvalidInputError) as excinfo:
        reverse(None)
    assert str(excinfo.value) == 'Expected "str", received "NoneType"'
