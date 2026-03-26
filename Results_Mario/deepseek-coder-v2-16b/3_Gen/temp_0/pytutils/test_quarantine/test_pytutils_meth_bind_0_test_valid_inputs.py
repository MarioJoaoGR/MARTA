
import pytest
from pytutils.meth import bind

class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def test_valid_inputs():
    foo = Foo(2, 3)
    mymethod = lambda self: self.x * self.y
    
    bind(foo, mymethod, 'multiply')
    
    assert hasattr(foo, 'multiply'), "Method not bound correctly"
    assert callable(getattr(foo, 'multiply')), "Bound method is not callable"
    assert foo.multiply() == 6, "Incorrect result from bound method"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_meth_bind_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_meth_bind_0_test_valid_inputs.py:18:11: E1101: Instance of 'Foo' has no 'multiply' member (no-member)


"""