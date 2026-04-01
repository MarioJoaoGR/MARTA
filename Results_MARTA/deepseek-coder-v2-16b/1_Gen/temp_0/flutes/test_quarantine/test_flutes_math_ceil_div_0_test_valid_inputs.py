
import pytest
from flutes.math import ceil_div

def test_valid_inputs():
    # Test cases for valid inputs
    assert ceil_div(10, 3) == 4
    assert ceil_div(-7, 2) == -3
    assert ceil_div(5, -2) == -2
    assert ceil_div(0, 5) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_math_ceil_div_0_test_valid_inputs.py F  [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test cases for valid inputs
        assert ceil_div(10, 3) == 4
        assert ceil_div(-7, 2) == -3
>       assert ceil_div(5, -2) == -2
E       assert -1 == -2
E        +  where -1 = ceil_div(5, -2)

flutes/Test4DT_tests/test_flutes_math_ceil_div_0_test_valid_inputs.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_math_ceil_div_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""