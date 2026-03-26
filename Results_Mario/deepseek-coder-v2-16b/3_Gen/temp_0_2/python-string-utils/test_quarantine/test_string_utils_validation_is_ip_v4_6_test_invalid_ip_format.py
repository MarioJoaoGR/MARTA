
import pytest
from string_utils.validation import is_ip_v4, SHALLOW_IP_V4_RE, is_full_string

@pytest.mark.parametrize("ip", [
    'nope',          # Not an IP address
    '255.200.100.75.', # Missing segment
    '255.200..75',   # Double dot
    '255.200.100',  # Missing segment
    '255.200.100.999', # Out of range segment
    '256.200.100.75', # Segment out of range
    '00.00.00.00',   # Leading zeros
    '-1.-1.-1.-1',  # Negative numbers
])
def test_invalid_ip_format(ip):
    assert not is_ip_v4(ip)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 8 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_6_test_invalid_ip_format.py . [ 12%]
.....F.                                                                  [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_ip_format[00.00.00.00] ______________________

ip = '00.00.00.00'

    @pytest.mark.parametrize("ip", [
        'nope',          # Not an IP address
        '255.200.100.75.', # Missing segment
        '255.200..75',   # Double dot
        '255.200.100',  # Missing segment
        '255.200.100.999', # Out of range segment
        '256.200.100.75', # Segment out of range
        '00.00.00.00',   # Leading zeros
        '-1.-1.-1.-1',  # Negative numbers
    ])
    def test_invalid_ip_format(ip):
>       assert not is_ip_v4(ip)
E       AssertionError: assert not True
E        +  where True = is_ip_v4('00.00.00.00')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_6_test_invalid_ip_format.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_6_test_invalid_ip_format.py::test_invalid_ip_format[00.00.00.00]
========================= 1 failed, 7 passed in 0.04s ==========================
"""