
from string_utils.validation import is_full_string, SHALLOW_IP_V4_RE

def test_valid_ipv4():
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('nope') == False
    assert is_ip_v4('255.200.100.999') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_ip_v4_5_test_valid_ipv4
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_5_test_valid_ipv4.py:5:11: E0602: Undefined variable 'is_ip_v4' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_5_test_valid_ipv4.py:6:11: E0602: Undefined variable 'is_ip_v4' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_5_test_valid_ipv4.py:7:11: E0602: Undefined variable 'is_ip_v4' (undefined-variable)


"""