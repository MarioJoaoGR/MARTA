
import re
import pytest
from string_utils.validation import is_ip_v4, is_ip_v6

def test_invalid_ip():
    # Test cases with invalid IPs
    assert not is_ip("1.2.3")  # Invalid IPv4 address
    assert not is_ip("not an ip")  # Not an IP address
    assert not is_ip("2001:db8:85a3::0000:8a2e:370:7334")  # Invalid IPv6 address with extra colon
    assert not is_ip("2001:db8:85a3:0000:0000:8a2e:370:7334:extra")  # Invalid IPv6 address with too many segments

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_ip_2_test_invalid_ip
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_2_test_invalid_ip.py:8:15: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_2_test_invalid_ip.py:9:15: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_2_test_invalid_ip.py:10:15: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_2_test_invalid_ip.py:11:15: E0602: Undefined variable 'is_ip' (undefined-variable)


"""