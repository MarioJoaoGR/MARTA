
import pytest
from pytutils.sets import TimedValueSet
import time

@pytest.fixture
def timed_value_set():
    return TimedValueSet(_store=set(), _meta={}, _initial=None, _meta_func=lambda value, **kwargs: time.time())

def test_added_at(timed_value_set):
    assert hasattr(timed_value_set, '_meta')
    assert timed_value_set.added_at() == timed_value_set._meta

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

pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_edge_case.py E [100%]

==================================== ERRORS ====================================
_______________________ ERROR at setup of test_added_at ________________________

    @pytest.fixture
    def timed_value_set():
>       return TimedValueSet(_store=set(), _meta={}, _initial=None, _meta_func=lambda value, **kwargs: time.time())
E       TypeError: TimedValueSet.__init__() got an unexpected keyword argument '_store'

pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_edge_case.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_edge_case.py::test_added_at
=============================== 1 error in 0.07s ===============================
"""