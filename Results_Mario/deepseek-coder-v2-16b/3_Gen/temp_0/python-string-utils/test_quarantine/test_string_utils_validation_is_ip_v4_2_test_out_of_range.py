
import re
import pytest
from string_utils.validation import is_full_string, SHALLOW_IP_V4_RE

def test_out_of_range():
    # Test cases for numbers out of the valid range for an IPv4 address
    assert not is_ip_v4('255.200.100.999')  # number out of range
    assert not is_ip_v4('256.200.100.75')   # first number out of range
    assert not is_ip_v4('255.200.100')      # not enough numbers
    assert not is_ip_v4('nope')             # not an IP address

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_ip_v4_2_test_out_of_range
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_2_test_out_of_range.py:8:15: E0602: Undefined variable 'is_ip_v4' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_2_test_out_of_range.py:9:15: E0602: Undefined variable 'is_ip_v4' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_2_test_out_of_range.py:10:15: E0602: Undefined variable 'is_ip_v4' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_2_test_out_of_range.py:11:15: E0602: Undefined variable 'is_ip_v4' (undefined-variable)


"""