
import pytest
from pymonet.utils import eq

def test_invalid_inputs():
    # Test with None values
    assert not eq(None, 5)
    assert not eq(5, None)
    assert eq(None, None)
    
    # Test with different types but same value (e.g., int and float that represent the same number)
    assert not eq(1, 1.0)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_utils_eq_2_test_invalid_inputs.py F   [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with None values
        assert not eq(None, 5)
        assert not eq(5, None)
        assert eq(None, None)
    
        # Test with different types but same value (e.g., int and float that represent the same number)
>       assert not eq(1, 1.0)
E       assert not True
E        +  where True = eq(1, 1.0)

pyMonet/Test4DT_tests/test_pymonet_utils_eq_2_test_invalid_inputs.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_eq_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.06s ===============================
"""