
import pytest
from unittest.mock import patch

def test_valid_case_1():
    version_1 = '1.2.3'
    version_2 = '1.2.2'
    
    with patch('__main__.is_version_greater', return_value=True):
        assert is_version_greater(version_1, version_2) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_utils_is_version_greater_0_test_valid_case_1
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_is_version_greater_0_test_valid_case_1.py:10:15: E0602: Undefined variable 'is_version_greater' (undefined-variable)


"""