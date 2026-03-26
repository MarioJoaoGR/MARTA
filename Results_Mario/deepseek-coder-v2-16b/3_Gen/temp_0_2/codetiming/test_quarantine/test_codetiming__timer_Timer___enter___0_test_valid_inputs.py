
import pytest
from codetiming import Timer
from typing import Optional, Union, Callable, ClassVar
from dataclasses import field
import math
import time

class Timers:
    pass  # Placeholder for actual implementation of Timers class

class TimerError(Exception):
    pass  # Placeholder for actual implementation of TimerError class

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Timer(name="test", text=123, initial_text="start", logger=None)

    with pytest.raises(TypeError):
        Timer(name=None, text="Elapsed time: {:0.4f} seconds", initial_text=True, logger=print)

    with pytest.raises(TypeError):
        Timer(name=None, text="Elapsed time: {:0.4f} seconds", initial_text="start", logger="logger")

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_valid_inputs.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_valid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.02s ===============================
"""