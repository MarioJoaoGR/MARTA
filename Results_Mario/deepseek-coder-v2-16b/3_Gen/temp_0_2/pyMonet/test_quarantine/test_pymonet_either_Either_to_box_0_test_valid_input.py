
import pytest
from pymonet.either import Either

def test_valid_input():
    # Test with a valid integer value
    either = Either(10)
    box = either.to_box()
    assert isinstance(box, Box)
    assert box.value == 10

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_either_Either_to_box_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_either_Either_to_box_0_test_valid_input.py:9:27: E0602: Undefined variable 'Box' (undefined-variable)


"""