
import pytest
from ansible.module_utils.api import basic_auth_argument_spec

def test_basic_auth_argument_spec_with_valid_dict():
    spec = {
        'timeout': dict(type='int', default=30)
    }
    result = basic_auth_argument_spec(spec)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert 'api_username' in result, "Expected 'api_username' to be in the result"
    assert 'api_password' in result, "Expected 'api_password' to be in the result"
    assert 'api_url' in result, "Expected 'api_url' to be in the result"
    assert 'validate_certs' in result, "Expected 'validate_certs' to be in the result"
    assert 'timeout' in result, "Expected 'timeout' to be in the result"
    assert result['timeout']['type'] == 'int', "The type of 'timeout' should be int"
    assert result['timeout']['default'] == 30, "The default value for 'timeout' should be 30"

def test_basic_auth_argument_spec_without_custom():
    result = basic_auth_argument_spec()
    assert isinstance(result, dict), "The result should be a dictionary"
    assert 'api_username' in result, "Expected 'api_username' to be in the result"
    assert 'api_password' in result, "Expected 'api_password' to be in the result"
    assert 'api_url' in result, "Expected 'api_url' to be in the result"
    assert 'validate_certs' in result, "Expected 'validate_certs' to be in the result"
    assert not hasattr(result, 'timeout'), "There should be no custom timeout argument if none is provided"
