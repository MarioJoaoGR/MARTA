
from string_utils.validation import is_ip_v4, is_ip_v6

def test_valid_ipv4():
    # Valid IPv4 addresses
    assert is_ip_v4('255.200.100.75') == True
    assert is_ip_v4('192.168.1.1') == True
    assert is_ip_v4('0.0.0.0') == True
    assert is_ip_v4('255.255.255.255') == True
    
    # Invalid IPv4 addresses
    assert is_ip_v4('1.2.3') == False
    assert is_ip_v4('1.2.3.4.5') == False
    assert is_ip_v4('256.256.256.256') == False
    assert is_ip_v4('000.000.000.000') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_0_test_valid_ipv4.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_ipv4 ________________________________

    def test_valid_ipv4():
        # Valid IPv4 addresses
        assert is_ip_v4('255.200.100.75') == True
        assert is_ip_v4('192.168.1.1') == True
        assert is_ip_v4('0.0.0.0') == True
        assert is_ip_v4('255.255.255.255') == True
    
        # Invalid IPv4 addresses
        assert is_ip_v4('1.2.3') == False
        assert is_ip_v4('1.2.3.4.5') == False
        assert is_ip_v4('256.256.256.256') == False
>       assert is_ip_v4('000.000.000.000') == False
E       AssertionError: assert True == False
E        +  where True = is_ip_v4('000.000.000.000')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_0_test_valid_ipv4.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_0_test_valid_ipv4.py::test_valid_ipv4
============================== 1 failed in 0.03s ===============================
"""