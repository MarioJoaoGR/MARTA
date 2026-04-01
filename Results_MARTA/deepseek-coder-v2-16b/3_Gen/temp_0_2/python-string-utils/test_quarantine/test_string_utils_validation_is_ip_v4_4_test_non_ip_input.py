
import pytest
from string_utils.validation import is_full_string, SHALLOW_IP_V4_RE

def test_non_ip_input():
    input_string = 'nope'
    assert not is_ip_v4(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_ip_v4_4_test_non_ip_input
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_4_test_non_ip_input.py:7:15: E0602: Undefined variable 'is_ip_v4' (undefined-variable)


"""