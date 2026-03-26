
import pytest
from unittest.mock import patch
from io import StringIO
from pytutils.memo import _lazyprop

@pytest.fixture
def MyClass():
    class MyClass:
        def __init__(self, value):
            self.value = value
        
        @_lazyprop
        def lazy_attribute(self):
            print("Computing the attribute...")
            return self.value * 2
    
    return MyClass

def test_valid_input(MyClass):
    obj = MyClass(10)
    assert obj.lazy_attribute == 20
    # The value is already computed, so it won't recompute
    assert obj.lazy_attribute == 20

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo__lazyprop_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_memo__lazyprop_0_test_valid_input.py:5:0: E0611: No name '_lazyprop' in module 'pytutils.memo' (no-name-in-module)


"""