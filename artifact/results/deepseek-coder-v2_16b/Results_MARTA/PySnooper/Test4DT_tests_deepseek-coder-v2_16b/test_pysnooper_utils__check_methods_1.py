
import pytest
from pysnooper.utils import _check_methods

# Test valid methods scenario
def test_valid_methods():
    class A:
        def meth1(self): pass
        def meth2(self): pass

    class B(A):
        def meth1(self): pass  # Inherits from A
        def meth3(self): pass

    assert _check_methods(B, 'meth1', 'meth2', 'meth3') == True

# Test missing methods scenario

# Test invalid input scenario