
# Module: pytutils.ext.rwclassproperty
import pytest
from classproperty import ClassPropertyMeta, rwclassproperty

# Example 1: Simple Read-Write Property
class Z(object, metaclass=ClassPropertyMeta):
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

def test_simple_read_write_property():
    assert Z.foo == 123
    assert Z.bar is None
    Z.bar = 222
    assert Z.bar == 222

# Example 2: Read-Only Property
class ZReadOnly(object, metaclass=ClassPropertyMeta):
    @rwclassproperty
    def foo(cls):
        return 123
    
    # _bar is not initialized here, so accessing bar will raise an AttributeError
    @rwclassproperty
    def bar(cls):
        return cls._bar

def test_read_only_property():
    with pytest.raises(AttributeError):
        ZReadOnly.bar  # Accessing a read-only property should raise an AttributeError

# Example 3: Setting a Property with Initial Value
class ZWithInitialValue(object, metaclass=ClassPropertyMeta):
    @rwclassproperty
    def foo(cls):
        return 123
    
    _bar = None  # Initialize the property with a default value
    
    @rwclassproperty
    def bar(cls):
        return cls._bar
    
    @bar.setter
    def bar(cls, value):
        cls._bar = value

def test_setting_initial_value():
    assert ZWithInitialValue.foo == 123
    assert ZWithInitialValue.bar is None
    ZWithInitialValue.bar = 222
    assert ZWithInitialValue.bar == 222

# Example 4: Using `rwclassproperty` with Different Getter and Setter Functions
class ZDifferentGetterSetter(object, metaclass=ClassPropertyMeta):
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

def test_different_getter_and_setter():
    assert ZDifferentGetterSetter.foo == 123
    assert ZDifferentGetterSetter.bar is None
    ZDifferentGetterSetter.bar = 222
    assert ZDifferentGetterSetter.bar == 222

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty___get___0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:4:0: E0401: Unable to import 'classproperty' (import-error)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:9:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:15:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:19:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:31:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:36:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:37:15: E1101: Instance of 'ZReadOnly' has no '_bar' member; maybe 'bar'? (no-member)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:46:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:52:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:56:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:68:4: E0213: Method 'foo' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:74:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty___get___0.py:78:4: E0213: Method 'bar' should have "self" as first argument (no-self-argument)


"""