# Module: pysnooper.utils
import pytest
from pysnooper.utils import WritableStream

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

class BaseWriter:
    def write(self, data):
        print(data)

class DerivedWriter(BaseWriter):
    pass

class NonWriter:
    def read(self, data):
        return data

class NullWriter:
    write = None

def test_writablestream_subclasshook_with_write_method():
    assert WritableStream.__subclasshook__(BaseWriter) is True

def test_writablestream_subclasshook_inherited_write_method():
    assert WritableStream.__subclasshook__(DerivedWriter) is True

def test_writablestream_subclasshook_without_write_method():
    assert WritableStream.__subclasshook__(NonWriter) is NotImplemented

def test_writablestream_subclasshook_with_object():
    assert WritableStream.__subclasshook__(object) is NotImplemented

def test_writablestream_subclasshook_with_write_set_to_none():
    assert WritableStream.__subclasshook__(NullWriter) is NotImplemented
