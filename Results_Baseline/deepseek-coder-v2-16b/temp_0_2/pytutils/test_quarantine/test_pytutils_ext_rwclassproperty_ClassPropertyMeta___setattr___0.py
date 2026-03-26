
# Module: pytutils.ext.rwclassproperty
import pytest
from pytutils.ext.rwclassproperty import ClassPropertyMeta, classproperty

# Define a class using ClassPropertyMeta as metaclass
class MyClass(metaclass=ClassPropertyMeta):
    @classproperty
    def my_property(cls):
        return "Hello, World!"

def test_access_class_property():
    assert MyClass.my_property == "Hello, World!"

def test_attempt_to_set_class_property():
    with pytest.raises(AttributeError) as e:
        MyClass.my_property = "New Value"
    assert str(e.value) == "'MyClass' object has no attribute 'my_property'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_ClassPropertyMeta___setattr___0
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_ClassPropertyMeta___setattr___0.py:9:4: E0213: Method 'my_property' should have "self" as first argument (no-self-argument)


"""