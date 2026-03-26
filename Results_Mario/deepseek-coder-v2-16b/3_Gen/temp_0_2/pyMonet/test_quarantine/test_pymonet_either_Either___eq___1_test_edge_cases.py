
import pytest
from pymonet.either import Either, Left, Right

def test_edge_cases():
    # Test equality with a Left instance
    left1 = Left("error message")
    either1 = Either(left1)
    
    left2 = Left("another error message")
    either2 = Either(left2)
    
    assert either1 == either2  # Both are Left instances with different values
    
    # Test equality with a Right instance
    right_value = Right(42)
    either3 = Either(right_value)
    
    assert either1 != either3  # one is Left, the other is Right
    
    # Test equality with another type of object
    wrong_object = "not an Either instance"
    assert either1 != wrong_object  # not an Either instance

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

pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test equality with a Left instance
        left1 = Left("error message")
        either1 = Either(left1)
    
        left2 = Left("another error message")
        either2 = Either(left2)
    
>       assert either1 == either2  # Both are Left instances with different values
E       assert <pymonet.either.Either object at 0x7fe731ecb450> == <pymonet.either.Either object at 0x7fe730d2a350>

pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___1_test_edge_cases.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either___eq___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""