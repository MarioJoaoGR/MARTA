
import pytest
from ansible.module_utils.api import basic_auth_argument_spec

def test_basic_auth_argument_spec_with_custom_spec():
    custom_spec = {
        'timeout': dict(type='int', default=30)
    }
    arg_spec = basic_auth_argument_spec(custom_spec)
    assert isinstance(arg_spec['api_username'], dict) and arg_spec['api_username']['type'] == 'str'
    assert isinstance(arg_spec['api_password'], dict) and arg_spec['api_password']['type'] == 'str' and arg_spec['api_password'].get('no_log') is True
    assert isinstance(arg_spec['api_url'], dict) and arg_spec['api_url']['type'] == 'str'
    assert isinstance(arg_spec['validate_certs'], dict) and arg_spec['validate_certs']['type'] == 'bool' and arg_spec['validate_certs'].get('default') is True
    assert isinstance(arg_spec['timeout'], dict) and arg_spec['timeout']['type'] == 'int' and arg_spec['timeout'].get('default') == 30

def test_basic_auth_argument_spec_without_custom_spec():
    arg_spec = basic_auth_argument_spec()
    assert isinstance(arg_spec['api_username'], dict) and arg_spec['api_username']['type'] == 'str'
    assert isinstance(arg_spec['api_password'], dict) and arg_spec['api_password']['type'] == 'str' and arg_spec['api_password'].get('no_log') is True
    assert isinstance(arg_spec['api_url'], dict) and arg_spec['api_url']['type'] == 'str'
    assert isinstance(arg_spec['validate_certs'], dict) and arg_spec['validate_certs']['type'] == 'bool' and arg_spec['validate_certs'].get('default') is True
