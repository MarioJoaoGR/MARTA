
# Module: pytutils.ext.rwclassproperty
import pytest
from classproperty import ClassPropertyMeta, rwclassproperty

# Example 1: Read-Only Class Property
class Z(object, metaclass=ClassPropertyMeta):
    @rwclassproperty
    def foo(cls):
        return 123

def test_read_only_class_property():
    assert Z.foo == 123
    with pytest.raises(AttributeError):
        Z.foo = 456

# Example 2: Read-Write Class Property
class Z(object, metaclass=ClassPropertyMeta):
    _bar = None
    
    @rwclassproperty
    def bar(cls):
        return cls._bar
    
    @bar.setter
    def bar(cls, value):
        cls._bar = value

def test_read_write_class_property():
    assert Z.bar == None  # Initial value should be None
    Z.bar = 222  # Set the property to a new value
    assert Z.bar == 222

# Example 3: Using `rwclassproperty` with Custom Getter and Setter
class Z(object, metaclass=ClassPropertyMeta):
    _baz = None
    
    @rwclassproperty
    def baz(cls):
        return cls._baz
    
    @baz.setter
    def baz(cls, value):
        cls._baz = value

def test_custom_getter_and_setter():
    assert Z.baz == None  # Initial value should be None
    Z.baz = 333  # Set the property to a new value
    assert Z.baz == 333

# Example 4: Using `rwclassproperty` with No Setter for Read-Only Property
class Z(object, metaclass=ClassPropertyMeta):
    _qux = None
    
    @rwclassproperty
    def qux(cls):
        return cls._qux

def test_no_setter():
    assert Z.qux == None  # Initial value should be None
    with pytest.raises(AttributeError):
        Z.qux = 789

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___init___0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:4:0: E0401: Unable to import 'classproperty' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:9:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:18:0: E0102: class already defined line 7 (function-redefined)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:22:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:26:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:35:0: E0102: class already defined line 7 (function-redefined)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:39:4: E0213: Method 'baz' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:43:4: E0213: Method 'baz' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:52:0: E0102: class already defined line 7 (function-redefined)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___init___0.py:56:4: E0213: Method 'qux' should have "self" as first argument (no-self-argument)


"""