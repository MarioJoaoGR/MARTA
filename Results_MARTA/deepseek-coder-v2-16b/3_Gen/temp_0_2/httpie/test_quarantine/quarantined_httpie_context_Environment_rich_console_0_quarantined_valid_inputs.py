
import unittest
from unittest.mock import patch
from httpie.context import Environment

class TestEnvironment(unittest.TestCase):
    @patch('httpie.context.sys')
    def test_rich_console(self, mock_sys):
        # Mock sys.stdout to simulate a terminal environment
        mock_sys.stdout = unittest.mock.Mock()
        mock_sys.stdout.isatty.return_value = True
        
        env = Environment()
        console = env.rich_console()
        
        self.assertIsNotNone(console)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_context_Environment_rich_console_0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_rich_console_0_test_valid_inputs.py:14:18: E1102: env.rich_console is not callable (not-callable)


"""