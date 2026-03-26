
from string_utils.validation import is_ip, is_ip_v4, is_ip_v6

def test_valid_ipv6():
    # Test cases for valid IPv6 addresses
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    assert is_ip('fe80::1ff:fe23:4567:89ab') == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_0_test_valid_ipv6.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_ipv6 ________________________________

    def test_valid_ipv6():
        # Test cases for valid IPv6 addresses
        assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
>       assert is_ip('fe80::1ff:fe23:4567:89ab') == True
E       AssertionError: assert False == True
E        +  where False = is_ip('fe80::1ff:fe23:4567:89ab')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_0_test_valid_ipv6.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_0_test_valid_ipv6.py::test_valid_ipv6
============================== 1 failed in 0.03s ===============================
"""