
import pytest
from pytutils.env import load_env_file
import os
import collections
import typing

@pytest.fixture
def mock_lines():
    return ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

@pytest.fixture
def mock_environ(monkeypatch):
    env = {'HOME': '/home/user'}
    monkeypatch.setenv('HOME', '/home/user')
    return env

def test_load_env_file(mock_lines, mock_environ):
    result = load_env_file(mock_lines, write_environ=mock_environ)
    
    expected_result = collections.OrderedDict([
        ('TEST', '/home/user/yeee-$PATH'),
        ('THISIS', '/a/test'),
        ('YOLO', '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    ])
    
    assert result == expected_result
    assert mock_environ == {'TEST': '/home/user/yeee-$PATH', 'THISIS': '/a/test', 'YOLO': '/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""