
from isort.format import format_simplified
import pytest

def test_valid_case_from():
    assert format_simplified("from math import sqrt") == "math.sqrt"
    assert format_simplified("from math import sqrt, pi") == "math.sqrt,pi"

def test_valid_case_import():
    assert format_simplified("import os; import sys") == "os;sys"

def test_invalid_case():
    with pytest.raises(ValueError):
        format_simplified("")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_case_from.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_case_from _____________________________

    def test_valid_case_from():
        assert format_simplified("from math import sqrt") == "math.sqrt"
>       assert format_simplified("from math import sqrt, pi") == "math.sqrt,pi"
E       AssertionError: assert 'math.sqrt, pi' == 'math.sqrt,pi'
E         
E         - math.sqrt,pi
E         + math.sqrt, pi
E         ?           +

isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_case_from.py:7: AssertionError
____________________________ test_valid_case_import ____________________________

    def test_valid_case_import():
>       assert format_simplified("import os; import sys") == "os;sys"
E       AssertionError: assert 'os; sys' == 'os;sys'
E         
E         - os;sys
E         + os; sys
E         ?    +

isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_case_from.py:10: AssertionError
______________________________ test_invalid_case _______________________________

    def test_invalid_case():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_case_from.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_case_from.py::test_valid_case_from
FAILED isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_case_from.py::test_valid_case_import
FAILED isort/Test4DT_tests/test_isort_format_format_simplified_0_test_valid_case_from.py::test_invalid_case
============================== 3 failed in 0.10s ===============================
"""