
import pytest
from ansible.module_utils.common.parameters import DEFAULT_TYPE_VALIDATORS, _get_type_validator

# Define a mock for DEFAULT_TYPE_VALIDATORS to simulate predefined type validators
DEFAULT_TYPE_VALIDATORS = {
    'int': lambda x: isinstance(x, int),
    'str': lambda x: isinstance(x, str),
}

def test_get_type_validator_with_predefined_type():
    validator, type_name = _get_type_validator('int')
    assert callable(validator)
    assert type_name == 'int'

def test_get_type_validator_with_custom_callable():
    def custom_validator(value):
        return isinstance(value, (int, float))
    
    validator, type_name = _get_type_validator(custom_validator)
    assert callable(validator)
    assert type_name == 'custom_validator'

def test_get_type_validator_with_none():
    validator, type_name = _get_type_validator(None)
    assert callable(validator)
    assert type_name == 'str'
