
from pytutils.memo import _lazyprop  # Importing the lazyprop decorator correctly
import pytest

class MyClass:
    def __init__(self, value):
        self.value = value
    
    @_lazyprop
    def lazy_attribute(self):
        print("Computing the attribute...")
        return self.value * 2

def test_none_input():
    obj = MyClass(10)
    assert obj.lazy_attribute == 20
    # The value is already computed, so it won't recompute
    assert obj.lazy_attribute == 20

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo__lazyprop_0_test_none_input
pytutils/Test4DT_tests/test_pytutils_memo__lazyprop_0_test_none_input.py:2:0: E0611: No name '_lazyprop' in module 'pytutils.memo' (no-name-in-module)


"""