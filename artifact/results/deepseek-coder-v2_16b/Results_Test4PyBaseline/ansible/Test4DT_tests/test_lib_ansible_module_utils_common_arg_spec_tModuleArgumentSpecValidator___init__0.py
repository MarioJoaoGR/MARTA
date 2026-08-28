# Module: ansible.module_utils.common.arg_spec
# test_module_argument_spec_validator.py
from ansible.module_utils.basic import AnsibleModule
import pytest

@pytest.fixture
def module():
    argument_spec = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'default': 18}
    }
    return AnsibleModule(argument_spec=argument_spec)

@pytest.fixture
def validator(module):
    return module._argspec_validator

def test_validate_with_valid_params(validator):
    validated_params = {
        'name': 'John Doe',
        'age': 30,
    }
    result = validator.validate(validated_params)
    assert result is None, "Validation should pass for valid parameters"

def test_validate_with_deprecated_alias(validator):
    validated_params = {
        'name': 'John Doe',
        'age': 30,
        'alias': 'incorrect_name'  # This will be deprecated and trigger a warning
    }
    with pytest.warns(UserWarning, match="deprecated alias"):
        result = validator.validate(validated_params)
    assert result is None, "Validation should pass even if an alias is provided"

def test_validate_with_missing_required_param(validator):
    validated_params = {
        'age': 30,  # Missing required parameter 'name'
    }
    with pytest.raises(ValueError) as excinfo:
        validator.validate(validated_params)
    assert str(excinfo.value) == "'name' is a required argument", "Validation should fail for missing required parameters"
