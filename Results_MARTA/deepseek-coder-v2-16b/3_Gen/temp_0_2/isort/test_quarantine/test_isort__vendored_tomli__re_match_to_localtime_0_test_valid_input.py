
import pytest
import re
from time import struct_time, mktime
from isort._vendored.tomli._re import match_to_localtime

@pytest.fixture
def valid_match():
    return re.match(r'(\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,6}))?', '12:34:56.789')

def test_valid_input(valid_match):
    result = match_to_localtime(valid_match)
    expected_time = mktime(struct_time((1900, 1, 1, 12, 34, 56, 0, 1, -1))) + (789 * 1e-6)
    assert result == expected_time

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

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

valid_match = <re.Match object; span=(0, 12), match='12:34:56.789'>

    def test_valid_input(valid_match):
        result = match_to_localtime(valid_match)
        expected_time = mktime(struct_time((1900, 1, 1, 12, 34, 56, 0, 1, -1))) + (789 * 1e-6)
>       assert result == expected_time
E       assert datetime.time(12, 34, 56, 789000) == -2208941298.999211

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.12s ===============================
"""