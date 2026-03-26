
import os
import collections
import typing
import pytest
from pytutils.env import load_env_file

@pytest.fixture
def example_lines():
    return ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

def test_load_env_file(example_lines, monkeypatch):
    # Mock os.environ to capture changes
    env = {}
    monkeypatch.setattr(os, 'environ', env)
    
    result = load_env_file(example_lines, write_environ=env)
    
    assert isinstance(result, collections.OrderedDict)
    assert len(result) == 3
    assert result['TEST'] == os.path.expanduser('${HOME}/yeee-$PATH')
    assert result['THISIS'] == os.path.expanduser('~/a/test')
    assert result['YOLO'] == os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    
    # Check that the environment variables were updated correctly
    expected_env = {
        'TEST': os.path.expanduser('${HOME}/yeee-$PATH'),
        'THISIS': os.path.expanduser('~/a/test'),
        'YOLO': os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    }
    
    assert env == expected_env

def test_load_env_file_no_write(example_lines):
    result = load_env_file(example_lines, write_environ=None)
    
    assert isinstance(result, collections.OrderedDict)
    assert len(result) == 3