
import pytest
from pymonent.box import Box

def test_invalid_input():
    box = Box(10)
    with pytest.raises(TypeError):
        invalid_mapper = "not a callable"
        box.bind(invalid_mapper)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_bind_2_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_box_Box_bind_2_test_invalid_input.py:3:0: E0401: Unable to import 'pymonent.box' (import-error)


"""