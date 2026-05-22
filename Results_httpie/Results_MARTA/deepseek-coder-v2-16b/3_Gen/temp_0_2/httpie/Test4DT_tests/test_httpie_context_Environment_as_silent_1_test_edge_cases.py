
import unittest
from httpie.context import Environment
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path
from typing import Optional, IO, Iterator

class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.env = Environment()

    @patch('httpie.context.sys.stdout', new_callable=MagicMock)
    @patch('httpie.context.sys.stderr', new_callable=MagicMock)
    def test_as_silent(self, mock_stderr, mock_stdout):
        # Ensure the original stdout and stderr are not affected by the context manager
        self.env.stdout = mock_stdout
        self.env.stderr = mock_stderr

        with self.env.as_silent():
            self.assertEqual(self.env.stdout, self.env._devnull)
            self.assertEqual(self.env.stderr, self.env._devnull)

        # After the context manager exits, stdout and stderr should be restored to their original values
        self.assertIsNot(self.env.stdout, self.env._devnull)
        self.assertIsNot(self.env.stderr, self.env._devnull)
        self.assertEqual(self.env.stdout, mock_stdout)
        self.assertEqual(self.env.stderr, mock_stderr)

if __name__ == '__main__':
    unittest.main()
