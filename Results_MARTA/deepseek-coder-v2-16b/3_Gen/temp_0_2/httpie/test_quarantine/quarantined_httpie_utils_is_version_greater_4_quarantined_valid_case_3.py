
import pytest
from unittest.mock import patch

def test_valid_case_3():
    version_1 = '1.0.5'
    version_2 = '1.0.6'
    
    with patch('__main__.is_version_greater', return_value=False):
        assert not is_version_greater(version_1, version_2)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_is_version_greater_4_test_valid_case_3
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_is_version_greater_4_test_valid_case_3.py:10:19: E0602: Undefined variable 'is_version_greater' (undefined-variable)


"""