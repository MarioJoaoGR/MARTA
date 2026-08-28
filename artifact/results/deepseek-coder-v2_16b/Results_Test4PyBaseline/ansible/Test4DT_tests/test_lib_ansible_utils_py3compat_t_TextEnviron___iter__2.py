
import os
import sys
from ansible.utils.py3compat import _TextEnviron
import pytest

@pytest.fixture
def default_text_env():
    return _TextEnviron()

@pytest.fixture
def custom_text_env():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    return _TextEnviron(env=custom_env, encoding='utf-8')

# Test case to cover the __iter__ method directly
def test_default_iteration(default_text_env):
    iterator = iter(default_text_env)
    assert isinstance(iterator, type(iter(os.environ)))

def test_custom_iteration(custom_text_env):
    iterator = iter(custom_text_env)
    assert isinstance(iterator, type(iter(custom_text_env._raw_environ)))

# Test case to ensure the method returns an iterator that yields keys from the environment
def test_default_iteration_yields_keys(default_text_env):
    keys = [key for key in default_text_env]
    assert set(keys) == set(os.environ.keys())

def test_custom_iteration_yields_keys(custom_text_env):
    keys = [key for key in custom_text_env]
    assert set(keys) == set(custom_text_env._raw_environ.keys())
