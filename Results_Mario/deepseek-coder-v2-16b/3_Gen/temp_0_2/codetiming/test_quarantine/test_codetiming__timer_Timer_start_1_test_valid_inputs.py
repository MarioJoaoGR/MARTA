
import pytest
from codetiming import Timer
import time

class TimerError(Exception):
    """A custom exception used for timer errors."""
    pass

def test_valid_inputs():
    timer = Timer()
    
    with pytest.raises(TimerError) as excinfo:
        timer.start()
        
    assert str(excinfo.value) == "Timer is running. Use .stop() to stop it"
    
    # Additional test for logging initial text when name is provided
    timer = Timer(name="test_timer")
    with pytest.raises(TimerError) as excinfo:
        timer.start()
        
    assert str(excinfo.value) == "Timer is running. Use .stop() to stop it"
    
    # Additional test for logging initial text when name is not provided
    timer = Timer(initial_text="Initial text")
    with pytest.raises(TimerError) as excinfo:
        timer.start()
        
    assert str(excinfo.value) == "Timer is running. Use .stop() to stop it"

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        timer = Timer()
    
>       with pytest.raises(TimerError) as excinfo:
E       Failed: DID NOT RAISE <class 'Test4DT_tests.test_codetiming__timer_Timer_start_1_test_valid_inputs.TimerError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_1_test_valid_inputs.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.02s ===============================
"""