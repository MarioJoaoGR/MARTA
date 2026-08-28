
import pytest
from ansible.module_utils.api import basic_auth_argument_spec

def test_basic_auth_argument_spec_with_valid_spec():
    custom_spec = {
        'timeout': dict(type='int', default=30)
    }
    result = basic_auth_argument_spec(custom_spec)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert len(result) == 5, "The dictionary should have 5 key-value pairs"
    assert 'timeout' in result, "The dictionary should include the custom timeout argument"
    assert result['timeout'] == {'type': 'int', 'default': 30}, "The timeout argument specification is incorrect"

def test_basic_auth_argument_spec_without_custom_spec():
    result = basic_auth_argument_spec()
    expected_result = {
        'api_username': {'type': 'str'},
        'api_password': {'type': 'str', 'no_log': True},
        'api_url': {'type': 'str'},
        'validate_certs': {'type': 'bool', 'default': True}
    }
    assert result == expected_result, "The default argument specification is incorrect"
