
import pytest
from pymonet.box import Box
from pymonet.maybe import Maybe

def test_valid_input():
    box = Box(123)
    maybe_instance = box.to_maybe()
    
    assert isinstance(maybe_instance, Maybe)
    assert maybe_instance.is_just() is True
    assert maybe_instance.from_just() == 123

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_to_maybe_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_maybe_0_test_valid_input.py:11:11: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_maybe_0_test_valid_input.py:12:11: E1101: Instance of 'Maybe' has no 'from_just' member (no-member)


"""