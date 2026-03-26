
import pytest
from pymonet.box import Box
from pymonet.maybe import Maybe

def test_edge_case():
    box = Box(None)  # Creating a Box with None value
    maybe = box.to_maybe()
    
    assert maybe.is_just() is True
    assert maybe.value == None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_to_maybe_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_maybe_0_test_edge_case.py:10:11: E1101: Instance of 'Maybe' has no 'is_just' member (no-member)


"""