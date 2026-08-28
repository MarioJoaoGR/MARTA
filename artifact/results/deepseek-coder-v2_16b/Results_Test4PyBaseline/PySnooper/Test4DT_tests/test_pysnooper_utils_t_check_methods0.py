
import pytest
from pysnooper.utils import _check_methods

# Test cases for _check_methods function

def test_all_methods_present():
    class A: pass
    class B(A):
        def meth1(self): pass
        def meth2(self): pass
    
    class C(B): pass
    assert _check_methods(C, 'meth1', 'meth2') is True

def test_one_method_missing():
    class A: pass
    class B(A):
        def meth1(self): pass
    
    class C(B): pass
    assert _check_methods(C, 'meth1', 'meth2') == NotImplemented

def test_no_methods():
    class A: pass
    class B(A): pass
    
    class C(B): pass
    assert _check_methods(C, 'meth1', 'meth2') == NotImplemented

def test_one_method_is_none():
    class A: pass
    class B(A):
        def meth1(self): pass
        def meth2(self): None
    
    class C(B): pass