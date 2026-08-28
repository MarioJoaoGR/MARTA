
import pytest
from unittest.mock import patch
from ansible.module_utils.common.parameters import env_fallback, AnsibleFallbackNotFound

def test_env_fallback_single():
    with patch('os.environ', {'HOME': 'user_home'}):
        assert env_fallback('HOME') == 'user_home'


def test_env_fallback_not_found():
    with patch('os.environ', {}):
        with pytest.raises(AnsibleFallbackNotFound):
            env_fallback('HOME')
