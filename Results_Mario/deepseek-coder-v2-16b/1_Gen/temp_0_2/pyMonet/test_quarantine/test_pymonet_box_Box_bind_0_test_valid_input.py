
import pytest
from pymonent.box import Box

def test_valid_input():
    box = Box(10)
    mapped_value = box.bind(lambda x: x * 2)
    assert mapped_value == 20

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_bind_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_box_Box_bind_0_test_valid_input.py:3:0: E0401: Unable to import 'pymonent.box' (import-error)


"""