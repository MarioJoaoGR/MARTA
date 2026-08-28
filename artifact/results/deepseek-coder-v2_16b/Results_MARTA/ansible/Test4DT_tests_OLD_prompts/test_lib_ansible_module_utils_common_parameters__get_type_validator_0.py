
import pytest
from ansible.module_utils.common.parameters import _get_type_validator, DEFAULT_TYPE_VALIDATORS

def test__get_type_validator_with_predefined_type():
    validator, type_name = _get_type_validator('int')
    assert callable(validator), "Expected a callable function"
    assert type_name == 'int', "Expected the type name to be 'int'"

def test__get_type_validator_with_custom_callable():
    def custom_validator(value):
        return isinstance(value, (int, float))
    
    validator, type_name = _get_type_validator(custom_validator)
    assert callable(validator), "Expected a callable function"
    assert type_name == 'custom_validator', "Expected the type name to be 'custom_validator'"

def test__get_type_validator_with_none():
    validator, type_name = _get_type_validator(None)
    assert callable(validator), "Expected a callable function"
    assert type_name == 'str', "Expected the type name to be 'str'"
