
import unittest
from httpie.manager.__main__ import program
from environment import Environment
from exit_status import ExitStatus
from unittest.mock import patch

class TestProgram(unittest.TestCase):
    
    @patch('httpie.manager.__main__.sys')
    def test_valid_input(self, mock_sys):
        # Mock sys.argv to simulate command line arguments
        mock_sys.argv = ['program']
        
        # Call the program function with default environment
        result = program()
        
        # Assert that the exit status is SUCCESS for valid input
        self.assertEqual(result, ExitStatus.SUCCESS)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager___main___program_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_valid_input.py:4:0: E0401: Unable to import 'environment' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_valid_input.py:5:0: E0401: Unable to import 'exit_status' (import-error)


"""