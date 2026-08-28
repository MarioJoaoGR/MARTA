
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