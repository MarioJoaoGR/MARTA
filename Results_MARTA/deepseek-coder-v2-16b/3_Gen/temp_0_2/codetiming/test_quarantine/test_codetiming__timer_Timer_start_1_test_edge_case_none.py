
import pytest
from codetiming import Timer
import time

def test_edge_case_none():
    with pytest.raises(TypeError):
        timer = Timer()  # No arguments provided, should raise TypeError
        timer.start()     # Calling start without any arguments should also raise TypeError

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_1_test_edge_case_none.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer_start_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.02s ===============================
"""