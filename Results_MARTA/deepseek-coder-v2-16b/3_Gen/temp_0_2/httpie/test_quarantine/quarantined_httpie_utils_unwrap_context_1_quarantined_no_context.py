
import pytest
from unittest.mock import patch
from httpie.utils import unwrap_context, CustomException

def test_no_context():
    with patch('httpie.utils.unwrap_context', side_effect=lambda exc: None):
        try:
            raise CustomException("Test Exception")
        except CustomException as e:
            assert unwrap_context(e) is e

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_unwrap_context_1_test_no_context
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_unwrap_context_1_test_no_context.py:4:0: E0611: No name 'CustomException' in module 'httpie.utils' (no-name-in-module)


"""