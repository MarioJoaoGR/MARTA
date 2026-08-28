
import pytest
from ansible.module_utils.common.parameters import _get_type_validator, DEFAULT_TYPE_VALIDATORS

# Test cases for built-in type validators
def test_builtin_type_validator():
    result = _get_type_validator('int')
    assert callable(result[0]), "Expected a callable function"
    assert isinstance(result[1], str), "Expected a string representing the type name"
    assert result[1] == 'int', "Unexpected type name returned"

# Test cases for custom callables
def test_custom_callable():
    def custom_validator(value):
        return isinstance(value, str)
    
    result = _get_type_validator(custom_validator)
    assert callable(result[0]), "Expected a callable function"
    assert isinstance(result[1], str), "Expected a string representing the type name"
    assert result[1] == 'custom_validator', "Unexpected type name returned"

# Test cases for None as wanted type
def test_none_as_wanted_type():
    result = _get_type_validator(None)
    assert callable(result[0]), "Expected a callable function"
    assert isinstance(result[1], str), "Expected a string representing the type name"

# Test case for None as wanted type with default to 'str'
def test_none_as_wanted_type_default():
    result = _get_type_validator(None)
    assert callable(result[0]), "Expected a callable function"
    assert isinstance(result[1], str), "Expected a string representing the type name"