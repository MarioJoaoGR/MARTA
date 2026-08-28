
import pytest
from ansible.module_utils.common.parameters import DEFAULT_TYPE_VALIDATORS, _get_type_validator

# Test for predefined type validation
def test_get_type_validator_predefined():
    validator, type_name = _get_type_validator('int')
    assert callable(validator), "Expected a callable validator"
    assert type_name == 'int', "Expected type name to be 'int'"

# Test for custom callable validation
def test_get_type_validator_custom():
    def custom_validator(value):
        return isinstance(value, (int, float))
    
    validator, type_name = _get_type_validator(custom_validator)
    assert validator == custom_validator, "Expected the same callable to be returned"
    assert type_name == 'custom_validator', "Expected type name to be 'custom_validator'"

# Test for default validation when None is passed
def test_get_type_validator_default():
    validator, type_name = _get_type_validator(None)
    assert callable(validator), "Expected a callable validator"
    assert type_name == 'str', "Expected type name to be 'str'"
