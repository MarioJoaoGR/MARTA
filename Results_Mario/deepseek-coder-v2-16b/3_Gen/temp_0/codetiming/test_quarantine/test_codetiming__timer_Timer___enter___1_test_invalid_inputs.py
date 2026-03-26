
import pytest
from codetiming import Timer

def test_invalid_inputs():
    timer = Timer()
    
    # Test with a non-callable or non-string initial_text that is not bool
    with pytest.raises(TypeError):
        timer.initial_text = 123  # Invalid type, should raise TypeError
        with timer:
            pass

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

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        timer = Timer()
    
        # Test with a non-callable or non-string initial_text that is not bool
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___1_test_invalid_inputs.py:9: Failed
----------------------------- Captured stdout call -----------------------------
Timer started
Elapsed time: 0.0000 seconds
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___enter___1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.02s ===============================
"""