# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

def test_valid_string_input():
    formatter = __StringFormatter('hello world')
    assert formatter.input_string == 'hello world'

def test_another_valid_string_input():
    formatter = __StringFormatter('greetings, earthlings!')
    assert formatter.input_string == 'greetings, earthlings!'

def test_empty_string_input():
    formatter = __StringFormatter('')
    assert formatter.input_string == ''

def test_invalid_integer_input():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_invalid_float_input():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(123.456)
    assert str(excinfo.value) == 'Expected "str", received "float"'

def test_invalid_list_input():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(['hello', 'world'])
    assert str(excinfo.value) == 'Expected "str", received "list"'

def test_invalid_dict_input():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter({'key': 'value'})
    assert str(excinfo.value) == 'Expected "str", received "dict"'

def test_invalid_none_input():
    with pytest.raises(InvalidInputError) as excinfo:
        __StringFormatter(None)
    assert str(excinfo.value) == 'Expected "str", received "NoneType"'
