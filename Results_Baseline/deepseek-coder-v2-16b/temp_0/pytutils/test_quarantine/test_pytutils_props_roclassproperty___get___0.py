
# Module: pytutils.props
# test_roclassproperty.py
from pytutils.props import roclassproperty
import pytest

# Test 1: Define a read-only class property and access it as an attribute
class MyClass:
    @roclassproperty
    def my_attribute(cls):
        """Returns the name of the class."""
        return cls.__name__

@pytest.fixture(scope="module")
def create_instance():
    yield MyClass()

# Test accessing the property
def test_access_roclassproperty(create_instance):
    obj = create_instance
    assert obj.my_attribute == 'MyClass'

# Test attempting to set the property
def test_set_roclassproperty():
    with pytest.raises(AttributeError):
        MyClass().my_attribute = "new value"

# Test 2: Define a read-write class property and access/modify it through the class itself
from pytutils.ext.rwclassproperty import rwclassproperty

class Z(object):
    @rwclassproperty
    def foo(cls):
        return 123
    
    _bar = None
    
    @rwclassproperty
    def bar(cls):
        return cls._bar
    
    @bar.setter
    def bar(cls, value):
        cls._bar = value

# Test accessing and modifying the property through the class itself
def test_access_and_modify_rwclassproperty():
    assert Z.foo == 123
    assert Z.bar is None
    Z.bar = 222
    assert Z.bar == 222

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___get___0
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0.py:10:4: E0213: Method 'my_attribute' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0.py:12:15: E1101: Instance of 'MyClass' has no '__name__' member (no-member)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0.py:33:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0.py:39:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___get___0.py:43:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)


"""