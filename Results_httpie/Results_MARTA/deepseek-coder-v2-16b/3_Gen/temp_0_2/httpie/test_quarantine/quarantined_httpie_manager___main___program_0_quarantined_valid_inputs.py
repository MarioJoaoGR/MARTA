
import sys
from unittest.mock import patch
from httpie.manager.__main__ import program
from environment import Environment
from exit_status import ExitStatus

def test_valid_inputs():
    with patch('httpie.manager.__main__.Environment', return_value=Environment()):
        with patch('httpie.manager.__main__.ExitStatus', return_value=ExitStatus.SUCCESS):
            status = program(args=['arg1', 'arg2'])
            assert status == ExitStatus.SUCCESS

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_manager___main___program_0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager___main___program_0_test_valid_inputs.py:5:0: E0401: Unable to import 'environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager___main___program_0_test_valid_inputs.py:6:0: E0401: Unable to import 'exit_status' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager___main___program_0_test_valid_inputs.py:11:21: E1123: Unexpected keyword argument 'args' in function call (unexpected-keyword-arg)


"""