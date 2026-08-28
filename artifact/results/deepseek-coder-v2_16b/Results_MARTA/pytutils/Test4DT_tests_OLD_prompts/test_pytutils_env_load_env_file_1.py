
import pytest
import os
import typing
import collections
from unittest.mock import patch, MagicMock
from pytutils.env import load_env_file

# Scenario 1: Test standard input with valid environment variables
def test_valid_input():
    lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
    expected_output = collections.OrderedDict([('TEST', os.path.expanduser('${HOME}/yeee-$PATH')), 
                                                ('THISIS', os.path.expanduser('~/a/test')), 
                                                ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))])
    
    with patch('os.environ', {}):
        result = load_env_file(lines)
        assert result == expected_output

# Scenario 2: Test with None input to check error handling
def test_none_input():
    lines = None
    with pytest.raises(TypeError):
        load_env_file(lines)

# Scenario 3: Test with empty list as input to check error handling
def test_empty_list_input():
    lines = []
    expected_output = collections.OrderedDict()
    
    with patch('os.environ', {}):
        result = load_env_file(lines)
        assert result == expected_output

# Scenario 4: Test with invalid format input to check error handling
def test_invalid_format_input():
    lines = ['INVALIDFORMAT']
    expected_output = collections.OrderedDict()
    
    with patch('os.environ', {}):
        result = load_env_file(lines)
        assert result == expected_output
