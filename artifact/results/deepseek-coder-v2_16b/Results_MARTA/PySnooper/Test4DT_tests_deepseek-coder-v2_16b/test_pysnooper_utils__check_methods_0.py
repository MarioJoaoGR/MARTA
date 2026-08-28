
import pytest
from pysnooper.utils import _check_methods

def test_valid_methods_present():
    class A:
        def meth1(self): pass
        def meth2(self): pass

    class B(A):
        def meth3(self): pass

    assert _check_methods(B, 'meth1', 'meth2', 'meth3') == True

def test_missing_methods():
    class A:
        def meth1(self): pass

    class B(A):
        def meth2(self): pass

    assert _check_methods(B, 'meth1', 'meth2') == True

def test_nonexistent_methods():
    class A:
        def meth1(self): pass

    class B(A):
        pass

    assert _check_methods(B, 'meth1', 'meth2') == NotImplemented
