
import pytest
import os
import collections
import typing
from pytutils.env import load_env_file

# Test cases for load_env_file function
def test_load_env_file_default():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines)
    assert isinstance(result, collections.OrderedDict), "Expected OrderedDict"
    assert len(result) == 3, "Expected three key-value pairs"
    assert 'TEST' in result and os.path.expanduser('~') + '/yeee-' + os.getenv('PATH') == result['TEST'], "Unexpected value for TEST"
    assert 'THISIS' in result and os.path.expanduser('~/a/test') == result['THISIS'], "Unexpected value for THISIS"
    assert 'YOLO' in result and os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST') == result['YOLO'], "Unexpected value for YOLO"

def test_load_env_file_custom():
    custom_env = {'HOME': '/home/user', 'PATH': '/usr/bin'}
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines, write_environ=custom_env)
    assert isinstance(result, collections.OrderedDict), "Expected OrderedDict"
    assert len(result) == 3, "Expected three key-value pairs"