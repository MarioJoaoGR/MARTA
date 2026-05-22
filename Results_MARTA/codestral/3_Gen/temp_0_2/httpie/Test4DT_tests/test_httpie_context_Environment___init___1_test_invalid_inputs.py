
import unittest
from httpie.context import Environment
from unittest.mock import patch, MagicMock
import sys

class TestEnvironmentInit(unittest.TestCase):
    @patch('httpie.context.sys.stdin', new_callable=MagicMock)
    @patch('httpie.context.sys.stdout', new_callable=MagicMock)
    @patch('httpie.context.sys.stderr', new_callable=MagicMock)
    def test_invalid_inputs(self, mock_stderr, mock_stdout, mock_stdin):
        # Test invalid inputs by passing unexpected arguments to the Environment constructor
        with self.assertRaises(AssertionError):
            Environment(unexpected_arg='invalid')
