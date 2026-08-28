
import pytest
from ansible.utils.py3compat import _TextEnviron
import os
import sys

# Test initialization without parameters
def test_init_without_parameters():
    env = _TextEnviron()
    assert isinstance(env, _TextEnviron)
    assert env.encoding == sys.getfilesystemencoding()

# Test initialization with custom environment
def test_init_with_custom_environment():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    env = _TextEnviron(env=custom_env)
    assert isinstance(env, _TextEnviron)
    assert env.encoding == sys.getfilesystemencoding()

# Test initialization with specific encoding
def test_init_with_specific_encoding():
    utf8_env = _TextEnviron(encoding='utf-8')
    assert isinstance(utf8_env, _TextEnviron)
    assert utf8_env.encoding == 'utf-8'
    assert utf8_env._raw_environ == os.environ

# Test getting an environment variable
def test_get_environment_variable():
    env = _TextEnviron()
    os.environ['TEST_VAR'] = 'test_value'
    assert env['TEST_VAR'] == 'test_value'

# Test setting an environment variable
def test_set_environment_variable():
    env = _TextEnviron()
    with pytest.raises(TypeError):
        env['NEW_VAR'] = b'new_value'

# Test deleting an environment variable
def test_delete_environment_variable():
    env = _TextEnviron()
    os.environ['DELETE_VAR'] = 'delete_value'
    del env['DELETE_VAR']
    assert 'DELETE_VAR' not in env._raw_environ
