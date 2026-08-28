
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_string_input():
    formatter = __StringFormatter('Valid String')
    assert formatter.input_string == 'Valid String'

def test_edge_case_empty_string():
    formatter = __StringFormatter('')
    assert formatter.input_string == ''

def test_invalid_input_non_string():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'
