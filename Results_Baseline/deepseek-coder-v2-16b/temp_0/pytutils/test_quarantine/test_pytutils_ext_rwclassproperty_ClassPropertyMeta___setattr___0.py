
# Module: pytutils.ext.rwclassproperty
import pytest
from pytutils.ext.rwclassproperty import ClassPropertyMeta

# Test setting a new attribute that is not a class property
def test_set_new_attribute():
    obj = ClassPropertyMeta()
    with pytest.raises(AttributeError):
        obj.__setattr__('new_attr', 10)

# Test setting an existing attribute that is not a class property
def test_set_existing_non_class_property():
    obj = ClassPropertyMeta()
    obj.existing_attr = 5
    with pytest.raises(AttributeError):
        obj.__setattr__('existing_attr', 10)

# Test setting a class property
def test_set_class_property():
    class MyClass:
        @classmethod
        def my_attr(cls):
            return getattr(cls, '_my_attr', 42)
        
        @classmethod
        def my_attr(cls, value):
            cls._my_attr = value
    
    obj = MyClass()
    ClassPropertyMeta.__setattr__(obj, 'my_attr', 10)
    assert MyClass.my_attr() == 10

# Test setting a class property with incorrect metaclass
def test_set_class_property_incorrect_metaclass():
    class IncorrectMetaclass(type):
        pass
    
    class MyClass(metaclass=IncorrectMetaclass):
        @classmethod
        def my_attr(cls):
            return getattr(cls, '_my_attr', 42)
        
        @classmethod
        def my_attr(cls, value):
            cls._my_attr = value
    
    obj = MyClass()
    with pytest.raises(TypeError):
        ClassPropertyMeta.__setattr__(obj, 'my_attr', 10)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_ClassPropertyMeta___setattr___0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_ClassPropertyMeta___setattr___0.py:27:8: E0102: method already defined line 23 (function-redefined)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_ClassPropertyMeta___setattr___0.py:32:11: E1120: No value for argument 'value' in classmethod call (no-value-for-parameter)
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_ClassPropertyMeta___setattr___0.py:45:8: E0102: method already defined line 41 (function-redefined)


"""