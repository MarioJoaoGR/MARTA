
import pytest
from isort._vendored.tomli._re import match_to_localtime
import re

def test_none_input():
    with pytest.raises(TypeError):
        match_to_localtime(None)

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

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(TypeError):
>           match_to_localtime(None)

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_none_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

match = None

    def match_to_localtime(match: "re.Match") -> time:
>       hour_str, minute_str, sec_str, micros_str = match.groups()
E       AttributeError: 'NoneType' object has no attribute 'groups'

isort/isort/_vendored/tomli/_re.py:92: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_localtime_0_test_none_input.py::test_none_input
============================== 1 failed in 0.12s ===============================
"""