
import pytest
from pymonet.maybe import Maybe

def test_valid_input():
    maybe = Maybe(value=42, is_nothing=False)
    assert not maybe.is_nothing
    assert maybe.value == 42
    
    box = maybe.to_box()
    assert isinstance(box, Box)
    assert box.value == 42

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_maybe_Maybe_to_box_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_maybe_Maybe_to_box_0_test_valid_input.py:11:27: E0602: Undefined variable 'Box' (undefined-variable)


"""