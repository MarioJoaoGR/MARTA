
import pytest
from codetiming import Timer
import math

def test_edge_case():
    with pytest.raises(TypeError):  # Since __exit__ should accept three arguments (exc_type, exc_val, exc_tb)
        with Timer() as timer:
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

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
>       with pytest.raises(TypeError):  # Since __exit__ should accept three arguments (exc_type, exc_val, exc_tb)
E       Failed: DID NOT RAISE <class 'TypeError'>

codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_edge_case.py:7: Failed
----------------------------- Captured stdout call -----------------------------
Elapsed time: 0.0000 seconds
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_Timer___exit___1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.02s ===============================
"""