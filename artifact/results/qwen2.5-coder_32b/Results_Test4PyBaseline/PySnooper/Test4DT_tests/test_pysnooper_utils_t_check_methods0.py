# Module: pysnooper.utils
import pytest
from pysnooper.utils import _check_methods

class Base:
    def foo(self):
        pass

class Derived(Base):
    def bar(self):
        pass

class BaseWithNone:
    foo = None

class DerivedFromBaseWithNone(BaseWithNone):
    def bar(self):
        pass

class EmptyClass:
    pass

class MultiMethodClass:
    def method1(self):
        pass
    
    def method2(self):
        pass
    
    def method3(self):
        pass

def test_check_methods_all_present():
    assert _check_methods(Derived, 'foo', 'bar') is True

def test_check_methods_one_missing():
    assert _check_methods(Derived, 'foo', 'baz') is NotImplemented

def test_check_methods_explicitly_none():
    assert _check_methods(DerivedFromBaseWithNone, 'foo', 'bar') is NotImplemented

def test_check_methods_no_methods_in_class():
    assert _check_methods(EmptyClass, 'foo') is NotImplemented

def test_check_methods_multiple_methods():
    assert _check_methods(MultiMethodClass, 'method1', 'method2', 'method3') is True

def test_check_methods_single_method_present():
    assert _check_methods(Base, 'foo') is True

def test_check_methods_single_method_missing():
    assert _check_methods(EmptyClass, 'non_existent_method') is NotImplemented
