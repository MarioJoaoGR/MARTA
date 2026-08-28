# Module: ansible.utils.py3compat
import pytest
import os
import sys
from ansible.utils.py3compat import _TextEnviron

# Test default settings initialization
def test_default_settings():
    text_env = _TextEnviron()
    assert text_env._raw_environ == os.environ
    assert text_env.encoding == sys.getfilesystemencoding()

# Test custom environment dictionary and specific encoding initialization
@pytest.mark.parametrize("custom_env, expected_encoding", [
    ({'VAR1': 'value1', 'VAR2': 'value2'}, 'utf-8'),
    ({'VAR3': 'value3', 'VAR4': 'value4'}, 'latin-1')
])
def test_custom_environment_and_specific_encoding(custom_env, expected_encoding):
    text_env = _TextEnviron(env=custom_env, encoding=expected_encoding)
    assert text_env._raw_environ == custom_env
    assert text_env.encoding == expected_encoding
