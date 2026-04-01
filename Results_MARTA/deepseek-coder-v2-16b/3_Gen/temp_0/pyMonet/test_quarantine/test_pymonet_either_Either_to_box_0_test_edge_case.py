
import pytest
from pymonet.either import Either, Left, Right
from pymonet.box import Box

def test_edge_case():
    # Create a Left instance with an error message
    left_value = Left("error message")
    either_left = Either(left_value)
    
    # Create a Right instance with the value 42
    right_value = Right(42)
    either_right = Either(right_value)
    
    # Test transformation to Box for Left
    box_left = either_left.to_box()
    assert isinstance(box_left, Box)
    assert box_left.value == "error message"
    
    # Test transformation to Box for Right
    box_right = either_right.to_box()
    assert isinstance(box_right, Box)
    assert box_right.value == 42

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Create a Left instance with an error message
        left_value = Left("error message")
        either_left = Either(left_value)
    
        # Create a Right instance with the value 42
        right_value = Right(42)
        either_right = Either(right_value)
    
        # Test transformation to Box for Left
        box_left = either_left.to_box()
        assert isinstance(box_left, Box)
>       assert box_left.value == "error message"
E       AssertionError: assert <pymonet.either.Left object at 0x7f40f8457410> == 'error message'
E        +  where <pymonet.either.Left object at 0x7f40f8457410> = <pymonet.box.Box object at 0x7f40f8457450>.value

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_edge_case.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.09s ===============================
"""