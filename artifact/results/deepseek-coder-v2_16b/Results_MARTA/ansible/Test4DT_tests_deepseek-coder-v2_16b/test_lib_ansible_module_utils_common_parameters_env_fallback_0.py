
import os
import pytest
from ansible.module_utils.common.parameters import env_fallback, AnsibleFallbackNotFound

def test_env_fallback_single():
    # Test retrieving a value from a single environment variable
    os.environ['HOME'] = 'user_home'
    assert env_fallback('HOME') == 'user_home'


def test_env_fallback_not_found():
    # Test that an exception is raised when no environment variable is found
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NONEXISTENTVAR')