
import pytest
from ansible.module_utils.common.parameters import env_fallback
import os
from ansible.module_utils.errors import AnsibleFallbackNotFound

def test_env_fallback_single_variable():
    os.environ['HOME'] = 'user_home'
    assert env_fallback('HOME') == 'user_home'
    del os.environ['HOME']
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('HOME')


def test_env_fallback_no_variables():
    with pytest.raises(AnsibleFallbackNotFound):
        env_fallback('NONEXISTENT_VAR')