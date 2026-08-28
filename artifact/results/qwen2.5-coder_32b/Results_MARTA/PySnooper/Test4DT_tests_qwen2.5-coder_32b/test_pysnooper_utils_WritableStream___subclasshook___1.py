
import pytest

class WritableStream:
    @classmethod
    def __subclasshook__(cls, C):
        if cls is WritableStream:
            return _check_methods(C, 'write')
        return NotImplemented

def _check_methods(C, *methods):
    mro = C.__mro__
    for method in methods:
        for B in mro:
            if method in B.__dict__:
                if B.__dict__[method] is None:
                    return NotImplemented
                break
        else:
            return NotImplemented
    return True

class MyWritableClass:
    def write(self, data):
        pass

class NonWritableClass:
    pass

class PartiallyImplementedClass:
    write = None

def test_valid_class_with_write_method():
    C = MyWritableClass
    assert WritableStream.__subclasshook__(C) is True

def test_invalid_class_without_write_method():
    C = NonWritableClass
    assert WritableStream.__subclasshook__(C) is NotImplemented

def test_invalid_class_with_write_set_to_none():
    C = PartiallyImplementedClass
    assert WritableStream.__subclasshook__(C) is NotImplemented
