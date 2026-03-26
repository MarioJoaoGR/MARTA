
import pytest
from pytutils.memo import _lazyprop

class MyClass:
    def __init__(self, value):
        self.value = value
    
    @_lazyprop('cached_value', lambda self: self.value * 2)
    def double_value(self):
        pass

def test_invalid_input():
    obj = MyClass(5)
    with pytest.raises(AttributeError):
        # Attempt to access the property before it has been initialized
        obj.double_value()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo__lazyprop_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_memo__lazyprop_0_test_invalid_input.py:3:0: E0611: No name '_lazyprop' in module 'pytutils.memo' (no-name-in-module)


"""