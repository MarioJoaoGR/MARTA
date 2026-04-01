
import pytest
from pytutils.props import lazyperclassproperty

def test_invalid_input():
    class MyClass:
        @lazyperclassproperty
        def expensive_calculation(cls):
            # This should raise a TypeError if the input is invalid
            return "Result"
    
    with pytest.raises(TypeError):
        obj = MyClass()
        print(obj.expensive_calculation)  # Accessing the property should trigger the lazy evaluation and raise a TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyperclassproperty_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_invalid_input.py:8:8: E0213: Method 'expensive_calculation' should have "self" as first argument (no-self-argument)


"""