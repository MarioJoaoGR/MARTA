
import unittest
from httpie.context import Environment
from unittest.mock import patch
import sys
from io import StringIO

class TestEnvironment(unittest.TestCase):
    def test_as_silent(self):
        # Create a mock null device (devnull) for testing
        devnull = StringIO()
        
        with patch('sys.stdout', devnull), patch('sys.stderr', devnull):
            env = Environment(devnull=devnull)
            with env.as_silent():
                self.assertEqual(env.stdout, devnull)
                self.assertEqual(env.stderr, devnull)
        
        # Check that stdout and stderr are restored after the context is exited
        self.assertIsNot(env.stdout, devnull)
        self.assertIsNot(env.stderr, devnull)
