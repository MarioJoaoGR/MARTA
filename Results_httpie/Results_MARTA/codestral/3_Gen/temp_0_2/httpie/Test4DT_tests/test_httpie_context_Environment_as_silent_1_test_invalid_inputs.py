
import pytest
from unittest.mock import patch
from httpie.context import Environment

def test_invalid_inputs():
    with patch('httpie.context.sys.stdin', create=True) as mock_stdin, \
         patch('httpie.context.sys.stdout', create=True) as mock_stdout, \
         patch('httpie.context.sys.stderr', create=True) as mock_stderr:
        
        # Test with invalid stdin
        mock_stdin.isatty = lambda: False
        env = Environment()
        assert not hasattr(env, 'does_not_exist')

        # Test with invalid stdout
        mock_stdout.isatty = lambda: False
        env = Environment()
        assert not hasattr(env, 'does_not_exist')

        # Test with invalid stderr
        mock_stderr.isatty = lambda: False
        env = Environment()
        assert not hasattr(env, 'does_not_exist')
