
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

def test_default_initialization(default_text_env):
    assert isinstance(default_text_env.encoding, str)
    assert default_text_env._raw_environ == os.environ

def test_custom_initialization():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    text_env = _TextEnviron(env=custom_env, encoding='utf-8')
    assert text_env.encoding == 'utf-8'

def test_iter_method_default(default_text_env):
    # Test that the iterator returns keys from os.environ
    expected_keys = set(os.environ.keys())
    iter_result = list(default_text_env._raw_environ.__iter__())
    assert set(iter_result) == expected_keys

def test_iter_method_custom(custom_text_env):
    # Test that the iterator returns keys from the custom environment dictionary
    expected_keys = {'VAR1', 'VAR2'}
    iter_result = list(custom_text_env._raw_environ.__iter__())
    assert set(iter_result) == expected_keys
