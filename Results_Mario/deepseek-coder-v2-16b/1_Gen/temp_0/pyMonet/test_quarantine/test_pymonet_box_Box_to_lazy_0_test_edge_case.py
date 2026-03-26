
import pytest
from pymonet.box import Box
from pymonet.lazy import Lazy

def test_to_lazy():
    box = Box(42)
    lazy_box = box.to_lazy()
    assert isinstance(lazy_box, Lazy)
    assert lazy_box.fold() == 42

    string_box = Box("Hello, World!")
    lazy_string_box = string_box.to_lazy()
    assert isinstance(lazy_string_box, Lazy)
    assert lazy_string_box.fold() == "Hello, World!"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_box_Box_to_lazy_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_lazy_0_test_edge_case.py:10:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)
pyMonet/Test4DT_tests/test_pymonet_box_Box_to_lazy_0_test_edge_case.py:15:11: E1101: Instance of 'Lazy' has no 'fold' member (no-member)


"""