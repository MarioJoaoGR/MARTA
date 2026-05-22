
import pytest
from unittest.mock import patch
from httpie.manager.__main__ import program, ExitStatus

def test_invalid_input():
    with patch('sys.argv', ['httpie', '--invalid-option']):
        result = program()
        assert result == ExitStatus.ERROR_INVALID_ARGUMENTS

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager___main___program_0_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_invalid_input.py:9:25: E1101: Class 'ExitStatus' has no 'ERROR_INVALID_ARGUMENTS' member (no-member)


"""