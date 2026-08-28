
import pytest
from ansible.utils import py3compat as utils_py3compat

# Test for _TextEnviron initialization without parameters

# Test for _TextEnviron initialization with a custom environment dictionary

# Test for _TextEnviron initialization with a specific encoding
def test_text_environ_init_with_specific_encoding():
    text_env = utils_py3compat._TextEnviron(encoding='utf-8')
    assert hasattr(text_env, 'encoding')
    assert hasattr(text_env, '_raw_environ')
    assert hasattr(text_env, '_value_cache')
    assert isinstance(text_env.encoding, str)
    assert text_env.encoding == 'utf-8'

# Test for _TextEnviron iteration over environment variables
def test_text_environ_iteration():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    text_env = utils_py3compat._TextEnviron(env=custom_env)
    iterated_keys = [key for key in text_env]
    assert list(iterated_keys) == ['VAR1', 'VAR2']

# Test for _TextEnviron getting and setting environment variables

# Test for _TextEnviron deleting environment variables
def test_text_environ_delete():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    text_env = utils_py3compat._TextEnviron(env=custom_env)
    del text_env['VAR1']
    assert 'VAR1' not in text_env