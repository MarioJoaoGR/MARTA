
import pytest
from pytutils.props import lazyclassproperty

def test_invalid_input():
    class TestClass:
        @lazyclassproperty
        def expensive_calculation(cls):
            # This method should have "self" as first argument, but it doesn't because of the decorator usage error.
            pass
        
        @lazyclassproperty
        def invalid_method(cls):
            # This method also has a similar issue due to incorrect decorator usage.
            pass
    
    with pytest.raises(TypeError):
        TestClass.expensive_calculation  # Accessing the property should raise a TypeError because it doesn't take 'self' or 'cls'.
        
    with pytest.raises(TypeError):
        TestClass.invalid_method  # Similarly, accessing this method should also raise a TypeError.

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyclassproperty_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_invalid_input.py:8:8: E0213: Method 'expensive_calculation' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_lazyclassproperty_0_test_invalid_input.py:13:8: E0213: Method 'invalid_method' should have "self" as first argument (no-self-argument)


"""