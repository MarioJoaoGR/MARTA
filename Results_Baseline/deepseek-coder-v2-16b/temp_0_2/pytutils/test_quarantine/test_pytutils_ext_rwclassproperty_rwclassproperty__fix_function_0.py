
# Module: pytutils.ext.rwclassproperty
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty, ClassPropertyMeta

# Test cases for read-only property
def test_read_only_property():
    class MyClass(object, metaclass=ClassPropertyMeta):
        @classmethod
        @rwclassproperty
        def foo(cls):
            return 123
    
    # Accessing the read-only property should work without error
    assert MyClass.foo == 123
    
    # Attempting to set the property should raise an AttributeError
    with pytest.raises(AttributeError):
        MyClass.foo = 456

# Test cases for read-write property
def test_read_write_property():
    class MyClass(object, metaclass=ClassPropertyMeta):
        _bar = None
        
        @classmethod
        @rwclassproperty
        def bar(cls):
            return cls._bar
        
        @bar.setter
        def bar(cls, value):
            cls._bar = value
    
    # Accessing the property initially (should be None)
    assert MyClass.bar is None
    
    # Setting the property should work without error
    MyClass.bar = 222
    
    # Accessing the property after setting it should return the new value
    assert MyClass.bar == 222

# Test cases for invalid usage
def test_invalid_usage():
    with pytest.raises(TypeError):
        class InvalidClass(object, metaclass=ClassPropertyMeta):
            @classmethod
            @rwclassproperty
            def invalid_property(cls):
                return "This should raise a TypeError"
    
    # Ensure that the property is not created if it's not properly defined
    with pytest.raises(AttributeError):
        class InvalidSetterClass(object, metaclass=ClassPropertyMeta):
            _bar = None
            
            @classmethod
            @rwclassproperty
            def bar(cls):
                return cls._bar
    
    # Ensure that the property is not created if it's not properly defined
    with pytest.raises(AttributeError):
        class InvalidGetterClass(object, metaclass=ClassPropertyMeta):
            _bar = None
            
            @classmethod
            @rwclassproperty
            def bar():  # Missing 'cls' argument
                return cls._bar

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0.py:32:8: E0213: Method 'bar' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0.py:70:12: E0211: Method 'bar' has no argument (no-method-argument)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0.py:71:23: E0602: Undefined variable 'cls' (undefined-variable)


"""