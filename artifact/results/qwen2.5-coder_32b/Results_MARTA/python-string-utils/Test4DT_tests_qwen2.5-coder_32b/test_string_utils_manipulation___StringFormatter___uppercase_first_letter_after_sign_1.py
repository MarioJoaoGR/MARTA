
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_case():
    formatter = __StringFormatter('hello-world')
    assert formatter.input_string == 'hello-world'

def test_edge_case_empty_string():
    formatter = __StringFormatter('')
    assert formatter.input_string == ''

def test_invalid_input_non_string():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(None)
    assert str(excinfo.value) == 'Expected "str", received "NoneType"'
