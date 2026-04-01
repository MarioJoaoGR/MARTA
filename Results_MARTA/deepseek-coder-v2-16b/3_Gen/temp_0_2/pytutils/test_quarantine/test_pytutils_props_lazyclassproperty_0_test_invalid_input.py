
import pytest
from pytutils.props import lazyclassproperty

# Define a class with a lazyclassproperty
class MyClass:
    @lazyclassproperty
    def expensive_calculation(cls):
        print("Calculating...")
        return sum(range(1000))

def test_invalid_input():
    # Test that the method should have "self" as first argument
    with pytest.raises(TypeError):
        MyClass.expensive_calculation()  # This should raise a TypeError

    # Test that the method should have "cls" as first argument
    with pytest.raises(TypeError):
        MyClass.expensive_calculation(cls=MyClass)  # This should raise a TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyclassproperty_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_invalid_input.py:8:4: E0213: Method 'expensive_calculation' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_invalid_input.py:15:8: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""