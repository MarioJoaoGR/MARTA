
import pytest
from pytutils.sets import TimedValueSet
import time
import attr

@pytest.fixture
def timed_value_set():
    return TimedValueSet()

def test_added_at_initial(timed_value_set):
    # Initially, the added_at should be None or a default value
    assert timed_value_set.added_at() is not None

def test_added_at_after_setting_value(timed_value_set):
    initial_time = timed_value_set.added_at()
    # Set a value, which should update the added_at time
    timed_value_set.set_value("test_value")
    assert timed_value_set.added_at() > initial_time

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_edge_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_added_at_initial _____________________________

timed_value_set = TimedValueSet(_store=set(), _meta={}, _initial=None, _meta_func=<function TimedValueSet.<lambda> at 0x7f2b84b9bb00>)

    def test_added_at_initial(timed_value_set):
        # Initially, the added_at should be None or a default value
>       assert timed_value_set.added_at() is not None
E       TypeError: 'dict' object is not callable

pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_edge_case.py:13: TypeError
______________________ test_added_at_after_setting_value _______________________

timed_value_set = TimedValueSet(_store=set(), _meta={}, _initial=None, _meta_func=<function TimedValueSet.<lambda> at 0x7f2b84b9bb00>)

    def test_added_at_after_setting_value(timed_value_set):
>       initial_time = timed_value_set.added_at()
E       TypeError: 'dict' object is not callable

pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_edge_case.py:16: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_edge_case.py::test_added_at_initial
FAILED pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_edge_case.py::test_added_at_after_setting_value
============================== 2 failed in 0.07s ===============================
"""