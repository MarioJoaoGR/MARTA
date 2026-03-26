
import pytest
from pymonet.either import Either, Left, Right

def test_valid_input():
    # Create a valid input value
    valid_value = 42
    
    # Initialize an Either with a Right value
    either_instance = Either(Right(valid_value))
    
    # Convert the Either to a Box
    box_instance = either_instance.to_box()
    
    # Assert that the converted Box has the same value as the original Either
    assert box_instance.value == valid_value

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

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a valid input value
        valid_value = 42
    
        # Initialize an Either with a Right value
        either_instance = Either(Right(valid_value))
    
        # Convert the Either to a Box
        box_instance = either_instance.to_box()
    
        # Assert that the converted Box has the same value as the original Either
>       assert box_instance.value == valid_value
E       assert <pymonet.either.Right object at 0x7f403bbfd5d0> == 42
E        +  where <pymonet.either.Right object at 0x7f403bbfd5d0> = <pymonet.box.Box object at 0x7f403bc07390>.value

pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_valid_input.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.19s ===============================
"""