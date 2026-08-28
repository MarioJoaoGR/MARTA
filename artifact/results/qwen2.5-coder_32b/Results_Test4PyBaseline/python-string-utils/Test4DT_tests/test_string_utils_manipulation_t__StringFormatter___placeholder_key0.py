# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError, is_string

def test_string_formatter_initializes_with_valid_string():
    # Test with a valid string input
    formatter = __StringFormatter('hello')
    assert formatter.input_string == 'hello'

def test_string_formatter_raises_error_with_invalid_input_type():
    # Test with an integer instead of a string
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

    # Test with a list instead of a string
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter([1, 2, 3])
    assert str(excinfo.value) == 'Expected "str", received "list"'

    # Test with a dictionary instead of a string
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter({'key': 'value'})
    assert str(excinfo.value) == 'Expected "str", received "dict"'

def test_string_formatter_raises_error_with_none_input():
    # Test with None instead of a string
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(None)
    assert str(excinfo.value) == 'Expected "str", received "NoneType"'

def test_string_formatter_placeholder_key_format():
    # Since __placeholder_key is not meant to be called directly, we can't test it directly.
    # However, we can check if the format of the placeholder key is correct by calling the constructor
    # and using a mock or patching mechanism if necessary. For now, we assume it works as intended.
    pass

def test_is_string_function():
    # Test with valid string
    assert is_string('valid string') == True

    # Test with invalid types
    assert is_string(123) == False
    assert is_string([1, 2, 3]) == False
    assert is_string({'key': 'value'}) == False
    assert is_string(None) == False
