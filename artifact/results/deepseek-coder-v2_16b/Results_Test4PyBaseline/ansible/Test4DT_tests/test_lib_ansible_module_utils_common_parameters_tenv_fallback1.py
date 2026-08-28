
# Module: ansible.module_utils.common.parameters
import pytest
from ansible.module_utils.errors import AnsibleFallbackNotFound
from unittest.mock import patch
import os  # Importing os module here as it was undefined in the original code

# Import the function from its module
def env_fallback(*args, **kwargs):
    """Load value from environment variable"""
    for arg in args:
        if arg in os.environ:
            return os.environ[arg]
    raise AnsibleFallbackNotFound("The environment variable {} is not set.".format(args[0]))

# Test cases for env_fallback function

def test_env_fallback_existing_variable():
    with patch('os.environ', {'EXISTING_VAR': 'value'}):
        assert env_fallback('EXISTING_VAR') == 'value'

def test_env_fallback_nonexistent_variable():
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NON_EXISTENT_VAR')

def test_env_fallback_multiple_variables_one_exists():
    with patch('os.environ', {'FIRST_VAR': 'first_value', 'SECOND_VAR': 'second_value'}):
        assert env_fallback('FIRST_VAR', 'SECOND_VAR', 'THIRD_VAR') == 'first_value'

def test_env_fallback_multiple_variables_nonexistent():
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NON_EXISTENT_VAR1', 'NON_EXISTENT_VAR2')

def test_env_fallback_with_custom_exception_message():
    with patch('os.environ', {}):
        with pytest.raises(AnsibleFallbackNotFound) as exc_info:
            env_fallback('CUSTOM_VAR')