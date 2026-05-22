
import unittest
from httpie.context import Environment
from unittest.mock import patch, MagicMock
import sys

class TestEnvironmentStr(unittest.TestCase):
    @patch('sys.stdin', new_callable=MagicMock)
    @patch('sys.stdout', new_callable=MagicMock)
    @patch('sys.stderr', new_callable=MagicMock)
    def test_valid_inputs(self, mock_stderr, mock_stdout, mock_stdin):
        # Create an instance of Environment with default values
        env = Environment()
        
        # Test the __str__ method to ensure it returns a valid string representation
        str_env = str(env)
        self.assertIsInstance(str_env, str)
        for key in ['args', 'is_windows', 'config_dir', 'stdin', 'stdout', 'stderr', 'colors', 'program_name', 'show_displays']:
            self.assertIn(key, str_env)
        
        # Add more assertions to cover other attributes if needed
        # For example:
        # self.assertTrue(str_env.startswith('Environment'))

if __name__ == '__main__':
    unittest.main()
