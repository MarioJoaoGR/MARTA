
import pytest
import os
import sys
from ansible.utils.py3compat import _TextEnviron


def test_default_settings():
    # Test default settings (should use sys.getfilesystemencoding())
    env = {}
    text_env = _TextEnviron(env=env)
    assert text_env.encoding == sys.getfilesystemencoding()

def test_custom_environment():
    # Test with a custom environment dictionary and default encoding
    custom_env = {'KEY': 'value'}
    text_env = _TextEnviron(env=custom_env)
    assert len(text_env._raw_environ) == 1

def test_specific_encoding():
    # Test with a specific encoding
    utf8_env = _TextEnviron(encoding='utf-8')
    assert utf8_env.encoding == 'utf-8'