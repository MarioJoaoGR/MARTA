
import pytest
from ansible.module_utils.common.parameters import DEFAULT_TYPE_VALIDATORS, _get_type_validator

def test_get_type_validator_with_predefined_type():
    validator, type_name = _get_type_validator('int')
    assert callable(validator), "Expected a callable for 'int' but got None"
    assert type_name == 'int', f"Expected type name to be 'int' but got {type_name}"

def test_get_type_validator_with_custom_callable():
    def custom_validator(value):
        return isinstance(value, (int, float))
    
    validator, type_name = _get_type_validator(custom_validator)
    assert callable(validator), "Expected a callable but got None"
    assert type_name == 'custom_validator', f"Expected type name to be 'custom_validator' but got {type_name}"

def test_get_type_validator_with_none():
    validator, type_name = _get_type_validator(None)
    assert callable(validator), "Expected a callable for default type 'str' but got None"
    assert type_name == 'str', f"Expected type name to be 'str' but got {type_name}"
