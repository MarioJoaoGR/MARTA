
import pytest
from unittest.mock import patch
from httpie.context import Environment

def test_environment():
    with patch('sys.stdin', create=True) as mock_stdin, \
         patch('sys.stdout', create=True) as mock_stdout, \
         patch('sys.stderr', create=True) as mock_stderr:
        
        # Set up the environment variables for testing
        env = Environment(devnull=None, config_dir='/tmp/config')
        
        # Assert that the environment variables are set correctly
        assert env.config_dir == '/tmp/config'
        assert env.stdin is not None
        assert env.stdout is not None
        assert env.stderr is not None
        
        # Add more assertions as needed to cover other attributes and behaviors
