
import pytest
from ansible.utils.py3compat import _TextEnviron
import os
import sys

@pytest.fixture(scope="function")
def setup_text_env():
    return _TextEnviron()

@pytest.fixture(scope="function")
def setup_custom_env():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    return _TextEnviron(env=custom_env)

@pytest.fixture(scope="function")
def setup_utf8_env():
    return _TextEnviron(encoding='utf-8')


def test_custom_environment(setup_custom_env):
    text_env = setup_custom_env
    assert 'VAR1' in text_env and text_env['VAR1'] == 'value1', "Custom environment variables should be accessible"

def test_specific_encoding(setup_utf8_env):
    text_env = setup_utf8_env
    # Assuming 'KEY' is set to a byte string, it will be decoded using utf-8
    with pytest.raises(KeyError):
        value = text_env['KEY']  # This should raise KeyError because 'KEY' is not in the environment

def test_iteration(setup_text_env):
    text_env = setup_text_env
    for key in text_env:
        assert isinstance(key, str) and isinstance(text_env[key], str), "All keys and values should be strings"


def test_delete_variable(setup_text_env):
    text_env = setup_text_env
    with pytest.raises(KeyError):
        del text_env['VAR1']  # This should raise KeyError because 'VAR1' is not in the environment

def test_length_of_environment(setup_text_env):
    text_env = setup_text_env
    length = len(text_env)
    assert isinstance(length, int), "The number of items should be an integer"