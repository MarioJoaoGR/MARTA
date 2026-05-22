
import unittest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

class TestEnvironment(unittest.TestCase):
    def test_rich_console(self):
        with patch('httpie.context.sys') as mock_sys:
            # Mock sys.stdout to be a terminal (isatty=True)
            mock_sys.stdout = MagicMock()
            mock_sys.stdout.isatty.return_value = True
            
            env = Environment()
            rich_console = env.rich_console()
            
            # Assert that the rich_console method returns a Rich console object
            self.assertIsNotNone(rich_console)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_context_Environment_rich_console_2_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_rich_console_2_test_edge_cases.py:14:27: E1102: env.rich_console is not callable (not-callable)


"""