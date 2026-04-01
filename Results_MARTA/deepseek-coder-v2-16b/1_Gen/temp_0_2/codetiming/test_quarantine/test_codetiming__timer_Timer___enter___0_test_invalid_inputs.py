
import pytest
from codetiming import Timer
import math

def test_invalid_inputs():
    # Test case to ensure that TypeError is raised when invalid inputs are provided
    with pytest.raises(TypeError):
        with Timer() as timer:  # This should raise a TypeError if the constructor doesn't handle invalid inputs correctly
            pass  # The body of this context manager will not be executed due to the error being expected

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test case to ensure that TypeError is raised when invalid inputs are provided
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_invalid_inputs.py:8: Failed
----------------------------- Captured stdout call -----------------------------
Elapsed time: 0.0000 seconds
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.02s ===============================
"""