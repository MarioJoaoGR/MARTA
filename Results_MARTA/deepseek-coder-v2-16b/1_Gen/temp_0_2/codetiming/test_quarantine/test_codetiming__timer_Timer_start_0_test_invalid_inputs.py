
import pytest
from codetiming import Timer
import time
import math

def test_invalid_inputs():
    # Test with an unsupported type for initial_text
    with pytest.raises(TypeError):
        Timer(initial_text=42)  # 42 is an int, which should raise a TypeError

    # Test with a callable that does not accept float as argument for text
    def invalid_callable(arg):
        return "Invalid time: {}".format(arg)
    
    with pytest.raises(TypeError):
        Timer(text=invalid_callable)  # This should raise a TypeError because the callable expects a float but does not receive one

    # Test with an unsupported type for logger
    with pytest.raises(TypeError):
        Timer(logger="not_a_callable")  # "not_a_callable" is a string, which should raise a TypeError

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with an unsupported type for initial_text
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_0_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""