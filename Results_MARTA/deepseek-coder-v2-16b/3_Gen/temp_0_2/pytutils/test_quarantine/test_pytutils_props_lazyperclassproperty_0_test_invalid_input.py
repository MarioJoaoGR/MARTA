
import pytest
from pytutils.props import lazyperclassproperty

# Define the expensive calculation function
def expensive_calculation(cls):
    return cls()

@lazyperclassproperty(expensive_calculation)
def cached_instance(cls):
    pass

class MyClass1:
    pass

class MyClass2(MyClass1):
    pass

# Test cases for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        @lazyperclassproperty(lambda x: x)  # Invalid function signature, should raise TypeError
        def invalid_cached_instance(cls):
            pass

    with pytest.raises(AttributeError):
        class MyInvalidClass:
            pass
        with pytest.raises(AttributeError):
            print(MyInvalidClass.cached_instance)  # cached_instance should not be accessible on an invalid class

    assert not hasattr(MyClass1, 'cached_instance')  # Ensure the property is not initialized for MyClass1
    assert not hasattr(MyClass2, 'cached_instance')  # Ensure the property is not initialized for MyClass2

# Test cases to ensure separate instances per class/inheritor
def test_separate_instances():
    instance1 = MyClass1.cached_instance
    instance2 = MyClass2.cached_instance
    assert isinstance(instance1, MyClass1)  # Ensure the instance is of type MyClass1
    assert isinstance(instance2, MyClass2)  # Ensure the instance is of type MyClass2
    assert instance1 != instance2  # Ensure separate instances are created for different classes/inheritors

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyperclassproperty_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_invalid_input.py:30:18: E1101: Class 'MyInvalidClass' has no 'cached_instance' member (no-member)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_invalid_input.py:37:16: E1101: Class 'MyClass1' has no 'cached_instance' member (no-member)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_invalid_input.py:38:16: E1101: Class 'MyClass2' has no 'cached_instance' member (no-member)


"""