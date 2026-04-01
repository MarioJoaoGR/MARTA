
import pytest
from pymon.box import Box

def test_valid_input():
    box = Box(123)
    mapper = lambda x: str(x)
    
    # Apply the map function to the box value
    mapped_box = box.map(mapper)
    
    # Check if the mapped value is correct
    assert mapped_box.value == "123"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_map_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_box_Box_map_0_test_valid_input.py:3:0: E0401: Unable to import 'pymon.box' (import-error)


"""