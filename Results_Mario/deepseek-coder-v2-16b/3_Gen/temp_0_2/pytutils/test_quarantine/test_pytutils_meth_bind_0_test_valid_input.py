
import pytest
from pytutils.meth import bind

class Foo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def test_valid_input():
    foo = Foo(2, 3)
    my_unbound_method = lambda self: self.x * self.y
    
    bind(foo, my_unbound_method, 'multiply')
    
    assert hasattr(foo, 'multiply'), "The method was not bound correctly."
    assert callable(getattr(foo, 'multiply')), "The attribute is not a callable function."
    
    result = foo.multiply()
    assert result == 6, f"Expected 6 but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_meth_bind_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_meth_bind_0_test_valid_input.py:19:13: E1101: Instance of 'Foo' has no 'multiply' member (no-member)


"""