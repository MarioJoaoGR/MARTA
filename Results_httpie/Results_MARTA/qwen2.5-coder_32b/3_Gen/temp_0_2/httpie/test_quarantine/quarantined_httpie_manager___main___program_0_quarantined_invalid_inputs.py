
import pytest
from unittest.mock import patch
from httpie.manager.__main__ import program
from exit_status import ExitStatus

def test_invalid_inputs():
    with patch('sys.argv', ['httpie_manager', '--invalid_option']):
        result = program()
        assert result == ExitStatus.ERROR_INVALID_ARGS

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager___main___program_0_test_invalid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_invalid_inputs.py:5:0: E0401: Unable to import 'exit_status' (import-error)


"""