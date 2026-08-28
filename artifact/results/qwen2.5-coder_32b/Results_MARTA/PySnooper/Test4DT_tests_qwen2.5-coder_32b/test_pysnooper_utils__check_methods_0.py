
import pytest
from pysnooper.utils import _check_methods

# Define a simple class for testing
class MyClass:
    def foo(self):
        pass

# Define another class for testing
class AnotherClass:
    def bar(self):
        pass

# Define a class with multiple methods
class MultiMethodClass:
    def foo(self):
        pass
    def bar(self):
        pass

# Define a class with a method set to None
class NoneMethodClass:
    foo = None

# Define an abstract base class for testing
from abc import ABC, abstractmethod

class MyABC(ABC):
    @abstractmethod
    def required_method(self):
        pass

# Define a concrete subclass of the abstract base class
class ConcreteClass(MyABC):
    def required_method(self):
        pass

# Test function to check valid class with implemented methods
def test_valid_class_with_implemented_methods():
    assert _check_methods(MyClass, 'foo') is True

# Test function to check invalid class with missing methods
def test_invalid_class_with_missing_methods():
    assert _check_methods(AnotherClass, 'foo') is NotImplemented

# Test function to check valid class with multiple implemented methods
def test_valid_class_with_multiple_implemented_methods():
    assert _check_methods(MultiMethodClass, 'foo', 'bar') is True

# Test function to check invalid class with method set to None
def test_invalid_class_with_method_set_to_none():
    assert _check_methods(NoneMethodClass, 'foo') is NotImplemented

# Test function to check abstract base class with implemented methods
def test_abstract_base_class_with_implemented_methods():
    assert _check_methods(MyABC, 'required_method') is True

# Test function to check concrete subclass of abstract base class with implemented methods
def test_concrete_subclass_of_abc_with_implemented_methods():
    assert _check_methods(ConcreteClass, 'required_method') is True

# Test function to check invalid input (not a class type)
def test_invalid_inputs_not_a_class_type():
    with pytest.raises(AttributeError):
        _check_methods('not_a_class', 'only_one')
