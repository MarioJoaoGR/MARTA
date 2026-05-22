
import pytest
from unittest.mock import patch
from httpie.utils import unwrap_context, CustomException

def test_valid_input():
    with patch('httpie.utils.CustomException', new=CustomException):
        try:
            raise ValueError("Root error") from FileNotFoundError("Related error")
        except ValueError as e:
            unwrapped_exc = unwrap_context(e)
            assert isinstance(unwrapped_exc, ValueError), "Expected a ValueError but got something else"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_unwrap_context_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_unwrap_context_0_test_valid_input.py:4:0: E0611: No name 'CustomException' in module 'httpie.utils' (no-name-in-module)


"""