
import os
import sys
from ansible.utils.py3compat import _TextEnviron
import pytest

# Test case to check deletion of an existing key in the environment dictionary
def test_delitem_existing_key():
    text_env = _TextEnviron()
    original_length = len(text_env._raw_environ)
    del text_env['PATH']
    assert 'PATH' not in text_env._raw_environ, "Expected PATH to be deleted from the environment dictionary"
    assert len(text_env._raw_environ) == (original_length - 1), f"Expected length to decrease by one but got {len(text_env._raw_environ)}"

# Test case to check deletion of a non-existing key in the environment dictionary
def test_delitem_non_existing_key():
    text_env = _TextEnviron()
    with pytest.raises(KeyError):
        del text_env['NONEXISTINGKEY']

# Test case to check deletion of a key when the environment is empty
def test_delitem_empty_environment():
    text_env = _TextEnviron()
    # Manually set an empty dictionary for testing purposes
    text_env._raw_environ = {}
    with pytest.raises(KeyError):
        del text_env['ANYKEY']
