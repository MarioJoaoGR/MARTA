
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_string_initialization():
    formatter = __StringFormatter('hello world')
    assert formatter.input_string == 'hello world'

def test_invalid_input_error_handling():
    with pytest.raises(InvalidInputError):
        __StringFormatter(123)

