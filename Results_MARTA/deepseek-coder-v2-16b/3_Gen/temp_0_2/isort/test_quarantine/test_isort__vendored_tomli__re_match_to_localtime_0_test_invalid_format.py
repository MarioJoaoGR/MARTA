
import re
from time import struct_time, mktime, localtime
import pytest

def match_to_localtime(match: "re.Match") -> struct_time:
    hour_str, minute_str, sec_str, micros_str = match.groups()
    micros = int(micros_str.ljust(6, "0")) if micros_str else 0
    return mktime(struct_time((1900, 1, 1, int(hour_str), int(minute_str), int(sec_str), 0, 0, -1)))

def test_invalid_format():
    with pytest.raises(ValueError):
        match = re.match(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', "invalid input")
        match_to_localtime(match)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_invalid_format.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_format ______________________________

    def test_invalid_format():
        with pytest.raises(ValueError):
            match = re.match(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{3}))?', "invalid input")
>           match_to_localtime(match)

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_invalid_format.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

match = None

    def match_to_localtime(match: "re.Match") -> struct_time:
>       hour_str, minute_str, sec_str, micros_str = match.groups()
E       AttributeError: 'NoneType' object has no attribute 'groups'

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_invalid_format.py:7: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_invalid_format.py::test_invalid_format
============================== 1 failed in 0.09s ===============================
"""