
import pytest
from codetiming._timer import FloatArg

def test_valid_case():
    # Create an instance of FloatArg for testing
    float_arg = FloatArg()
    
    # Call the __call__ method with a valid float argument
    result = float_arg(3600.0)
    
    assert isinstance(result, FloatArg), "Expected the same instance of FloatArg"

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

codetiming/Test4DT_tests/test_codetiming__timer_FloatArg___call___0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        # Create an instance of FloatArg for testing
        float_arg = FloatArg()
    
        # Call the __call__ method with a valid float argument
>       result = float_arg(3600.0)
E       TypeError: 'FloatArg' object is not callable

codetiming/Test4DT_tests/test_codetiming__timer_FloatArg___call___0_test_valid_case.py:10: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED codetiming/Test4DT_tests/test_codetiming__timer_FloatArg___call___0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.02s ===============================
"""