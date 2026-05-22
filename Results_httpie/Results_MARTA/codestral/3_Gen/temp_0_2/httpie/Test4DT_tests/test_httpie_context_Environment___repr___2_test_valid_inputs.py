
import unittest
from httpie.context import Environment
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

class TestEnvironmentRepr(unittest.TestCase):
    @patch('httpie.context.sys')
    def test_valid_inputs(self, mock_sys):
        # Mocking necessary attributes for the Environment class
        mock_stdin = MagicMock()
        mock_stdout = MagicMock()
        mock_stderr = MagicMock()
        
        mock_sys.stdin = mock_stdin
        mock_sys.stdout = mock_stdout
        mock_sys.stderr = mock_stderr
        
        env = Environment(config_dir='/some/path')
        
        # Test the __repr__ method
        expected_repr = f'<Environment {env}>'
        self.assertEqual(expected_repr, repr(env))
