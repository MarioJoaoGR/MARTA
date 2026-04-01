
import pytest
from unittest.mock import patch
from pytutils.sets import TimedValueSet

@pytest.fixture
def timed_value_set():
    return TimedValueSet()

def test_valid_case(timed_value_set):
    with patch('time.time', return_value=1672502400.0):
        assert timed_value_set.added_at() == 1672502400.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

timed_value_set = TimedValueSet(_store=set(), _meta={}, _initial=None, _meta_func=<function TimedValueSet.<lambda> at 0x7fe5fa06f4c0>)

    def test_valid_case(timed_value_set):
        with patch('time.time', return_value=1672502400.0):
>           assert timed_value_set.added_at() == 1672502400.0
E           TypeError: 'dict' object is not callable

pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_valid_case.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.06s ===============================
"""