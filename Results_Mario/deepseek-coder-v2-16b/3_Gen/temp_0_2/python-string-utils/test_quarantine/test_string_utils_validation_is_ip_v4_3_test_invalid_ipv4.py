
import re
import pytest
from string_utils.validation import is_full_string, SHALLOW_IP_V4_RE

def test_invalid_ipv4():
    input_string = '255.200.100.999'
    assert not is_ip_v4(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_ip_v4_3_test_invalid_ipv4
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_3_test_invalid_ipv4.py:8:15: E0602: Undefined variable 'is_ip_v4' (undefined-variable)


"""