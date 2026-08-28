
import pytest
from ansible.module_utils.api import basic_auth_argument_spec

def test_basic_auth_argument_spec_default():
    """Test the default behavior of basic_auth_argument_spec."""
    expected_result = {
        'api_username': {'type': 'str'},
        'api_password': {'type': 'str', 'no_log': True},
        'api_url': {'type': 'str'},
        'validate_certs': {'type': 'bool', 'default': True}
    }
    assert basic_auth_argument_spec() == expected_result

def test_basic_auth_argument_spec_with_custom_spec():
    """Test adding custom specifications to the argument spec."""
    custom_spec = {'timeout': dict(type='int')}
    expected_result = {
        'api_username': {'type': 'str'},
        'api_password': {'type': 'str', 'no_log': True},
        'api_url': {'type': 'str'},
        'validate_certs': {'type': 'bool', 'default': True},
        'timeout': {'type': 'int'}
    }
    assert basic_auth_argument_spec(custom_spec) == expected_result

def test_basic_auth_argument_spec_incomplete_spec():
    """Test that incomplete specifications are handled gracefully."""
    # Test with a partial specification missing some defaults
    incomplete_spec = {
        'api_username': dict(type='str'),
        'api_password': dict(type='str', no_log=True),
        'api_url': dict(type='str')
    }
    expected_result = {
        'api_username': {'type': 'str'},
        'api_password': {'type': 'str', 'no_log': True},
        'api_url': {'type': 'str'},
        'validate_certs': {'type': 'bool', 'default': True}
    }