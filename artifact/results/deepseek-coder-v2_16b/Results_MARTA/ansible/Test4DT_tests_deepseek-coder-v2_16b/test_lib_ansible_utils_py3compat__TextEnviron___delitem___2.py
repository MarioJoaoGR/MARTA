
import pytest
from ansible.utils import py3compat

# Test initialization of _TextEnviron without parameters
def test_init_without_parameters():
    env = py3compat._TextEnviron()
    assert isinstance(env, py3compat._TextEnviron)
    assert hasattr(env, 'encoding')
    assert hasattr(env, '_raw_environ')
    assert hasattr(env, '_value_cache')

# Test initialization of _TextEnviron with a custom environment dictionary
def test_init_with_custom_environment():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    env = py3compat._TextEnviron(env=custom_env)
    assert isinstance(env, py3compat._TextEnviron)
    assert env['VAR1'] == 'value1'
    assert env['VAR2'] == 'value2'

# Test initialization of _TextEnviron with a specific encoding
def test_init_with_specific_encoding():
    utf8_env = py3compat._TextEnviron(encoding='utf-8')
    assert isinstance(utf8_env, py3compat._TextEnviron)
    assert utf8_env.encoding == 'utf-8'

# Test deletion of an environment variable using __delitem__
def test_delitem():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    env = py3compat._TextEnviron(env=custom_env)
    assert 'VAR1' in env._raw_environ
    del env['VAR1']
    assert 'VAR1' not in env._raw_environ
