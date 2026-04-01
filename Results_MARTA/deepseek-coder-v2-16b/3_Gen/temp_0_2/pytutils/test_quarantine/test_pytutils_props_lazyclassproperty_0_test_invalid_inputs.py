
import pytest
from pytutils.props import lazyclassproperty

# Define a class with a lazyclassproperty
class MyClass:
    @lazyclassproperty
    def expensive_calculation(cls):
        print("Calculating...")
        return sum(range(1000))

def test_invalid_inputs():
    # Test that the method has "self" as its first argument
    with pytest.raises(TypeError):
        MyClass.expensive_calculation()  # This should raise a TypeError because it doesn't have 'self'

    # Test that the method raises an error when called without arguments
    with pytest.raises(TypeError):
        MyClass().expensive_calculation()  # This should raise a TypeError because it expects 'cls' but gets 'self'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyclassproperty_0_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_invalid_inputs.py:8:4: E0213: Method 'expensive_calculation' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_invalid_inputs.py:15:8: E1120: No value for argument 'cls' in unbound method call (no-value-for-parameter)


"""