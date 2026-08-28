
import pytest
from pysnooper.utils import _check_methods

# Test valid methods scenario
def test_valid_methods():
    class A:
        def meth1(self): pass
        def meth2(self): pass

    class B(A):
        def meth3(self): pass

    assert _check_methods(B, 'meth1', 'meth2', 'meth3') is True

# Test missing method scenario
def test_missing_method():
    class A:
        def meth1(self): pass

    class B(A):
        def meth2(self): pass  # meth3 is not present in this subclass

    assert _check_methods(B, 'meth1', 'meth3') == NotImplemented

# Test method with None implementation scenario