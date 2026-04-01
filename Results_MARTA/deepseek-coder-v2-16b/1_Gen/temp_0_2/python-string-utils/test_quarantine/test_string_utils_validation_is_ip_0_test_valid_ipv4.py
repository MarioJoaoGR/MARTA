
# Importing necessary functions from string_utils.validation module
from string_utils.validation import is_ip_v4, is_ip_v6

def test_valid_ipv4():
    # Test valid IPv4 address
    assert is_ip('255.200.100.75') == True
    # Additional tests can be added here to cover different scenarios

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_ip_0_test_valid_ipv4
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_0_test_valid_ipv4.py:7:11: E0602: Undefined variable 'is_ip' (undefined-variable)


"""