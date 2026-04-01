
import pytest
from pytutils.props import lazyclassproperty

# Define a class with a lazyclassproperty
class MyClass:
    @lazyclassproperty
    def expensive_calculation(cls):
        print("Calculating...")
        return sum(range(1000))

def test_valid_inputs():
    # Test that the property is calculated only once
    instance = MyClass()
    result1 = MyClass.expensive_calculation
    assert 'Calculating...' in str(result1)  # First call should print "Calculating..."
    
    result2 = MyClass.expensive_calculation
    assert 'Calculating...' not in str(result2)  # Subsequent calls should not print "Calculating..."
    assert result2 == sum(range(1000))  # Check the cached value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyclassproperty_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_valid_inputs.py:8:4: E0213: Method 'expensive_calculation' should have "self" as first argument (no-self-argument)


"""