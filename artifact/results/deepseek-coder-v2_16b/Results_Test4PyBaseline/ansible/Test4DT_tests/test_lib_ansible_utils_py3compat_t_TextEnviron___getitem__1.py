
import os
import sys
from ansible.utils.py3compat import _TextEnviron
import pytest

def test__TextEnviron_getitem_existing_key():
    text_env = _TextEnviron()
    key = 'PATH'
    value = os.environ[key]
    assert text_env[key] == value, f"Expected {value} for key '{key}' but got {text_env[key]}"

def test__TextEnviron_getitem_nonexistent_key():
    text_env = _TextEnviron()
    key = 'NONEXISTENTKEY'
    assert key not in os.environ, "Key should not exist in environment"
    with pytest.raises(KeyError):
        text_env[key]

def test__TextEnviron_getitem_cached():
    text_env = _TextEnviron()
    key = 'PATH'
    value = os.environ[key]
    first_access = text_env[key]
    second_access = text_env[key]
    assert first_access == second_access, "Expected cached value to be returned on subsequent access"

def test__TextEnviron_getitem_encoding():
    custom_env = {'VAR1': 'value1'}
    text_env = _TextEnviron(env=custom_env, encoding='utf-8')
    assert text_env['VAR1'] == 'value1', "Expected value to be decoded according to specified encoding"

def test__TextEnviron_getitem_passthru():
    custom_env = {'VAR1': b'binaryvalue'}
    text_env = _TextEnviron(env=custom_env, encoding='utf-8')