
import pytest
from pymonit.box import Box

def test_edge_case():
    box = Box(None)
    with pytest.raises(TypeError):
        mapped_value = box.bind(lambda x: x * 2)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_bind_1_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_box_Box_bind_1_test_edge_case.py:3:0: E0401: Unable to import 'pymonit.box' (import-error)


"""