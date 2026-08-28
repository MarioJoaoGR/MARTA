
import os
from unittest.mock import patch
import pytest
from ansible.utils.py3compat import _TextEnviron

def test_custom_environment_dictionary():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    with patch.dict(os.environ, {}), pytest.raises(KeyError):
        env = _TextEnviron(env=custom_env)
        assert env['NON_EXISTENT_VAR'] == 'default_value'  # This should raise KeyError
