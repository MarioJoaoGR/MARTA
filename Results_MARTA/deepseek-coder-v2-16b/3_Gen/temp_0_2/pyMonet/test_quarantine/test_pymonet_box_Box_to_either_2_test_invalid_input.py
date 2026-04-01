
import pytest
from pymonet.box import Box
from pymonet.either import Right, Left

def test_invalid_input():
    # Test with a valid input
    box = Box(123)
    assert isinstance(box.to_either(), Right)
    
    # Test with an invalid input (None)
    invalid_box = Box(None)
    assert isinstance(invalid_box.to_either(), Left)

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

pyMonet/Test4DT_tests/test_pymonet_box_Box_to_either_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with a valid input
        box = Box(123)
        assert isinstance(box.to_either(), Right)
    
        # Test with an invalid input (None)
        invalid_box = Box(None)
>       assert isinstance(invalid_box.to_either(), Left)
E       assert False
E        +  where False = isinstance(<pymonet.either.Right object at 0x7fa262cc0fd0>, Left)
E        +    where <pymonet.either.Right object at 0x7fa262cc0fd0> = to_either()
E        +      where to_either = <pymonet.box.Box object at 0x7fa262cc03d0>.to_either

pyMonet/Test4DT_tests/test_pymonet_box_Box_to_either_2_test_invalid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_box_Box_to_either_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.09s ===============================
"""