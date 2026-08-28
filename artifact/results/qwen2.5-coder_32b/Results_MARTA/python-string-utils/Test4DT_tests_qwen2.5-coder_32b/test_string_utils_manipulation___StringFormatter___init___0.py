
import pytest
from string_utils.manipulation import __StringFormatter, is_string, InvalidInputError

def test___StringFormatter___init___basic():
    # Test with a valid string input
    formatter = __StringFormatter('hello')
    assert formatter.input_string == 'hello'

    # Test with an invalid input type (integer)
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'
