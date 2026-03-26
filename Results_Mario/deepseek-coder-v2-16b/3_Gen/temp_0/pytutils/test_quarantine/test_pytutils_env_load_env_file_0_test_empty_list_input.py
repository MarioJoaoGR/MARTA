
import pytest
from pytutils.env import load_env_file, parse_env_file_contents, expand
import os
import collections
import typing

@pytest.fixture
def env_lines():
    return ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']

def test_load_env_file(mocker, env_lines):
    # Mock os.environ to capture changes
    mocker.patch('os.environ', {})
    
    # Call the function with mocked lines and empty environment mapping
    result = load_env_file(env_lines, write_environ={})
    
    # Check that the returned OrderedDict has the correct expanded values
    assert isinstance(result, collections.OrderedDict)
    assert len(result) == 3
    assert result['TEST'] == os.path.expanduser('${HOME}/yeee-$PATH')
    assert result['THISIS'] == os.path.expanduser('~/a/test')
    assert result['YOLO'] == os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    
    # Check that the environment mapping was not modified
    assert len(os.environ) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""