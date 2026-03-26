
import re
import pytest
from string_utils.validation import is_ip_v4, is_ip_v6

def test_valid_ipv6():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('fe80::1ff:fe23:4567:89ab') == True
    assert is_ip('::1') == True
    assert is_ip('2001:db8:85a3:0:0:8A2E:370:7334') == True  # Case insensitive
    assert is_ip('2001:db8:85a3::8A2E:370:7334') == True  # Compressed form
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:0:7334') == True  # All zeros can be omitted
    assert is_ip('::ffff:192.168.1.1') == True  # IPv4-mapped address

def test_invalid_ipv6():
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370') == False  # Missing trailing segment
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334:9999') == False  # Too many segments
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:zzzz') == False  # Invalid characters
    assert is_ip('::ffff:192.168.1') == False  # Missing last segment

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_ip_1_test_valid_ipv6
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:7:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:8:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:9:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:10:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:11:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:12:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:13:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:16:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:17:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:18:11: E0602: Undefined variable 'is_ip' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_1_test_valid_ipv6.py:19:11: E0602: Undefined variable 'is_ip' (undefined-variable)


"""