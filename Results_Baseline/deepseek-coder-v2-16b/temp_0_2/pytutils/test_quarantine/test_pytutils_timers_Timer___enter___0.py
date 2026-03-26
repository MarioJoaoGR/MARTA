
import pytest
from pytutils.timers import Timer
import time

# Test cases for the Timer class

def test_basic_usage():
    with pytest.raises(NameError):  # Ensure no name provided raises an error
        with Timer('task_one'):
            pass

def test_verbose_mode():
    timer = None
    try:
        with Timer('important_function', verbose=True) as t:
            time.sleep(1)  # Simulate a task that takes some time
            assert isinstance(t, Timer), "Timer instance should be returned"
            assert hasattr(t, 'start'), "Timer instance should have a start attribute"
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

def test_decorator_usage():
    @Timer('decorated_function')
    def decorated_function():
        time.sleep(1)  # Simulate a function that takes some time
    
    decorated_function()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_timers_Timer___enter___0.py F.F     [100%]

=================================== FAILURES ===================================
_______________________________ test_basic_usage _______________________________

    def test_basic_usage():
>       with pytest.raises(NameError):  # Ensure no name provided raises an error
E       Failed: DID NOT RAISE <class 'NameError'>

pytutils/Test4DT_tests/test_pytutils_timers_Timer___enter___0.py:9: Failed
_____________________________ test_decorator_usage _____________________________

    def test_decorator_usage():
>       @Timer('decorated_function')
E       TypeError: 'Timer' object is not callable

pytutils/Test4DT_tests/test_pytutils_timers_Timer___enter___0.py:24: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_timers_Timer___enter___0.py::test_basic_usage
FAILED pytutils/Test4DT_tests/test_pytutils_timers_Timer___enter___0.py::test_decorator_usage
========================= 2 failed, 1 passed in 1.06s ==========================
"""