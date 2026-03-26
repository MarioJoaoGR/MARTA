
import pytest
from string_utils.validation import is_ip, is_ip_v4, is_ip_v6

@pytest.mark.parametrize("ip", [
    "255.200.100.75",  # Valid IPv4 address
    "2001:db8:85a3:0000:0000:8a2e:370:7334",  # Valid IPv6 address
    "1.2.3",  # Invalid IP address
])
def test_invalid_ip(ip):
    assert not is_ip(ip)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_2_test_invalid_ip.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_invalid_ip[255.200.100.75] ________________________

ip = '255.200.100.75'

    @pytest.mark.parametrize("ip", [
        "255.200.100.75",  # Valid IPv4 address
        "2001:db8:85a3:0000:0000:8a2e:370:7334",  # Valid IPv6 address
        "1.2.3",  # Invalid IP address
    ])
    def test_invalid_ip(ip):
>       assert not is_ip(ip)
E       AssertionError: assert not True
E        +  where True = is_ip('255.200.100.75')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_2_test_invalid_ip.py:11: AssertionError
____________ test_invalid_ip[2001:db8:85a3:0000:0000:8a2e:370:7334] ____________

ip = '2001:db8:85a3:0000:0000:8a2e:370:7334'

    @pytest.mark.parametrize("ip", [
        "255.200.100.75",  # Valid IPv4 address
        "2001:db8:85a3:0000:0000:8a2e:370:7334",  # Valid IPv6 address
        "1.2.3",  # Invalid IP address
    ])
    def test_invalid_ip(ip):
>       assert not is_ip(ip)
E       AssertionError: assert not True
E        +  where True = is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_2_test_invalid_ip.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_2_test_invalid_ip.py::test_invalid_ip[255.200.100.75]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_2_test_invalid_ip.py::test_invalid_ip[2001:db8:85a3:0000:0000:8a2e:370:7334]
========================= 2 failed, 1 passed in 0.04s ==========================
"""