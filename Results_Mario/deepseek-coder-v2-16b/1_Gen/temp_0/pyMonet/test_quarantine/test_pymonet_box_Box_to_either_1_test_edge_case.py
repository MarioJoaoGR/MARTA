
import pytest
from pymonet.box import Box

def test_edge_case():
    box = Box(None)
    assert box.value is None
    either = box.to_either()
    assert isinstance(either, Right)
    assert either.value is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_to_either_1_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_either_1_test_edge_case.py:9:30: E0602: Undefined variable 'Right' (undefined-variable)


"""