
import re
import pytest
from isort._vendored.tomli._re import match_to_number

# Test cases for match_to_number function
def test_match_to_number_integer():
    pattern = r'-?\d+'
    text = "The temperature was -123 today."
    m = re.search(pattern, text)
    assert match_to_number(m, int) == -123

def test_match_to_number_float():
    pattern = r'-?\d+(\.\d+)?'
    text = "The temperature was -123.45 today."
    m = re.search(pattern, text)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_number_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_match_to_number_integer _________________________

    def test_match_to_number_integer():
        pattern = r'-?\d+'
        text = "The temperature was -123 today."
        m = re.search(pattern, text)
>       assert match_to_number(m, int) == -123

isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_number_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

match = <re.Match object; span=(20, 24), match='-123'>
parse_float = <class 'int'>

    def match_to_number(match: "re.Match", parse_float: "ParseFloat") -> Any:
>       if match.group("floatpart"):
E       IndexError: no such group

isort/isort/_vendored/tomli/_re.py:98: IndexError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_number_0.py::test_match_to_number_integer
========================= 1 failed, 1 passed in 0.10s ==========================
"""