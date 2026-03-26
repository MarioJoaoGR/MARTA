
import pytest
import os
import collections
import typing
from pytutils.env import load_env_file

# Test cases for load_env_file function
def test_load_env_file_basic():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    result = load_env_file(lines)
    assert isinstance(result, collections.OrderedDict), "Expected OrderedDict"
    assert len(result) == 3, "Expected three key-value pairs"
    assert result['TEST'] == os.path.expandvars('${HOME}/yeee-$PATH'), f"Expected {os.path.expandvars('${HOME}/yeee-$PATH')} but got {result['TEST']}"
    assert result['THISIS'] == os.path.expanduser('~/a/test'), f"Expected {os.path.expanduser('~/a/test')} but got {result['THISIS']}"