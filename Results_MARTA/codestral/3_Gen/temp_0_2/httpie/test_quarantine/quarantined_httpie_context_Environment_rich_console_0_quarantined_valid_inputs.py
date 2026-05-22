
import unittest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

class TestEnvironment(unittest.TestCase):
    def test_rich_console(self):
        # Create a mock stdout and set its isatty to True for the purpose of this test
        mock_stdout = MagicMock()
        mock_stdout.isatty.return_value = True
        
        env = Environment()
        
        with patch('httpie.context.sys.stdout', mock_stdout):
            # Call the rich_console method and check if it returns a Rich console object
            rich_console = env.rich_console()
            self.assertIsNotNone(rich_console)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_context_Environment_rich_console_0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_context_Environment_rich_console_0_test_valid_inputs.py:16:27: E1102: env.rich_console is not callable (not-callable)


"""