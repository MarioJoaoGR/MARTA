
import pytest
from codetiming import Timer
import math

def test_edge_case():
    timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text=False, logger=print)
    with pytest.raises(Exception) as exc_info:
        timer.__exit__(None, None, None)
    assert "TimerError: The timer is not running and cannot be stopped." in str(exc_info.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/codetiming
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        timer = Timer(name=None, text='Elapsed time: {:0.4f} seconds', initial_text=False, logger=print)
        with pytest.raises(Exception) as exc_info:
            timer.__exit__(None, None, None)
>       assert "TimerError: The timer is not running and cannot be stopped." in str(exc_info.value)
E       AssertionError: assert 'TimerError: The timer is not running and cannot be stopped.' in 'Timer is not running. Use .start() to start it'
E        +  where 'Timer is not running. Use .start() to start it' = str(TimerError('Timer is not running. Use .start() to start it'))
E        +    where TimerError('Timer is not running. Use .start() to start it') = <ExceptionInfo TimerError('Timer is not running. Use .start() to start it') tblen=3>.value

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_edge_case.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================

"""