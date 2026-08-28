
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_case():
    formatter = __StringFormatter('hello   world')
    assert formatter.input_string == 'hello   world'

def test_edge_cases():
    # Test with an empty string
    formatter_empty = __StringFormatter('')
    assert formatter_empty.input_string == ''
    
    # Test with None should raise InvalidInputError
    with pytest.raises(InvalidInputError):
        __StringFormatter(None)

def test_invalid_case():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'
