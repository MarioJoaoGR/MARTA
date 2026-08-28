
import pytest
from string_utils.manipulation import camel_case_to_snake, InvalidInputError

def test_valid_camel_case():
    result = camel_case_to_snake('ThisIsACamelStringTest')
    assert result == 'this_is_a_camel_string_test'

def test_valid_camel_case_custom_separator():
    result = camel_case_to_snake('AnotherCamelCaseExample', '-')
    assert result == 'another-camel-case-example'

def test_non_camel_case_string():
    result = camel_case_to_snake('already_snake_case')
    assert result == 'already_snake_case'

def test_empty_string():
    result = camel_case_to_snake('')
    assert result == ''

def test_none_input():
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(None)

def test_integer_input():
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(123)
