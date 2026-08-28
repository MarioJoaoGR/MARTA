# Module: ansible.utils.py3compat
import os
import sys
from ansible.module_utils.py3compat import _TextEnviron
import pytest

# Test default settings initialization
def test_default_settings():
    text_env = _TextEnviron()
    assert isinstance(text_env, _TextEnviron)
    assert text_env.encoding == sys.getfilesystemencoding()
    assert text_env._raw_environ == os.environ

# Test initialization with custom environment dictionary and encoding
def test_custom_settings():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    text_env = _TextEnviron(env=custom_env, encoding='utf-8')
    assert isinstance(text_env, _TextEnviron)
    assert text_env.encoding == 'utf-8'
    assert text_env._raw_environ == custom_env

# Test setting an environment variable
def test_setitem():
    text_env = _TextEnviron()
    text_env['NEW_VAR'] = 'new_value'
    assert 'NEW_VAR' in text_env._raw_environ
    assert text_env._raw_environ['NEW_VAR'] == b'new_value'

# Test getting an environment variable
def test_getitem():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    text_env = _TextEnviron(env=custom_env, encoding='utf-8')
    assert text_env['VAR1'] == b'value1'

# Test deleting an environment variable
def test_delitem():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    text_env = _TextEnviron(env=custom_env, encoding='utf-8')
    del text_env['VAR1']
    assert 'VAR1' not in text_env._raw_environ
