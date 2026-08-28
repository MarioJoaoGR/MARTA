
import pytest
from pysnooper.utils import _check_methods

def test_valid_inheritance():
    class A:
        def meth1(self): pass
        def meth2(self): pass

    class B(A):
        def meth3(self): pass

    result = _check_methods(B, 'meth1', 'meth3')
    assert result is True

def test_method_presence():
    class A:
        def meth1(self): pass

    class B(A):
        def meth1(self): pass  # Inherits from A
        def meth2(self): pass

    result = _check_methods(B, 'meth1', 'meth2')
    assert result is True

def test_method_absence():
    class A:
        def meth1(self): pass

    class B(A):
        def meth2(self): pass  # Meth3 is not present in this subclass

    result = _check_methods(B, 'meth1', 'meth3')
    assert result is NotImplemented

def test_custom_class():
    class CustomClass:
        pass

    result = _check_methods(CustomClass, 'meth1', 'meth2')
    assert result is NotImplemented
