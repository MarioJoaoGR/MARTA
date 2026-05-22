
import unittest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

class TestEnvironment(unittest.TestCase):
    def test_rich_console(self):
        # Create a mock stdout and set its isatty to True for the sake of this test
        mock_stdout = MagicMock()
        mock_stdout.isatty.return_value = True
        
        env = Environment()
        
        with patch('httpie.context.sys.stdout', new=mock_stdout):
            console = env.rich_console()
            
            # Assert that the rich_console method returns a Rich console object
            self.assertIsNotNone(console)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_context_Environment_rich_console_1_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_rich_console_1_test_valid_inputs.py:15:22: E1102: env.rich_console is not callable (not-callable)


"""