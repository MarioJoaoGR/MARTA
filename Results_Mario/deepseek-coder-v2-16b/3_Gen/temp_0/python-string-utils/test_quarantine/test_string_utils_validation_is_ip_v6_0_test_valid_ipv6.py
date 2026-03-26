
import re
from string_utils.validation import is_full_string, IP_V6_RE

def test_valid_ipv6():
    input_string = '2001:db8:85a3:0000:0000:8a2e:370:7334'
    assert is_ip_v6(input_string) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_ip_v6_0_test_valid_ipv6
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v6_0_test_valid_ipv6.py:7:11: E0602: Undefined variable 'is_ip_v6' (undefined-variable)


"""