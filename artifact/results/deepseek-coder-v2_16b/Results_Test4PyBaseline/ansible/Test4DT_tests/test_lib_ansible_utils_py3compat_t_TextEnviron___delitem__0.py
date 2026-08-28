# Module: ansible.utils.py3compat
import os
import sys
import pytest
from ansible.utils.py3compat import _TextEnviron

# Test default configuration initialization
def test_default_configuration():
    text_env = _TextEnviron()
    assert isinstance(text_env, _TextEnviron), "Instance should be of type _TextEnviron"
    # Check if the encoding is set to sys.getfilesystemencoding()
    assert text_env.encoding == sys.getfilesystemencoding(), f"Expected {sys.getfilesystemencoding()} but got {text_env.encoding}"
    # Accessing a value from the environment (should return text string)
    path_value = text_env['PATH']
    assert isinstance(path_value, str), "The value should be a string"

# Test initialization with custom environment dictionary and encoding
def test_custom_configuration():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    text_env = _TextEnviron(env=custom_env, encoding='utf-8')
    assert isinstance(text_env, _TextEnviron), "Instance should be of type _TextEnviron"
    # Check if the specified encoding is used
    assert text_env.encoding == 'utf-8', f"Expected 'utf-8' but got {text_env.encoding}"
    # Accessing a value from the environment (should return text string)
    var1_value = text_env['VAR1']
    assert isinstance(var1_value, str), "The value should be a string"
    # Deleting an item from the environment
    del text_env['VAR2']
    assert 'VAR2' not in text_env._raw_environ, "Expected VAR2 to be deleted from the environment dictionary"

# Test initialization using os.environ and specified encoding
def test_os_environ_configuration():
    if 'PYTHONIOENCODING' in os.environ:
        del os.environ['PYTHONIOENCODING']  # Ensure PYTHONIOENCODING is not set to affect the test
    text_env = _TextEnviron(encoding='utf-8')
    assert isinstance(text_env, _TextEnviron), "Instance should be of type _TextEnviron"
    # Check if the specified encoding is used
    assert text_env.encoding == 'utf-8', f"Expected 'utf-8' but got {text_env.encoding}"
    # Accessing a value from the environment (should return text string)
    path_value = text_env['PATH']
    assert isinstance(path_value, str), "The value should be a string"
