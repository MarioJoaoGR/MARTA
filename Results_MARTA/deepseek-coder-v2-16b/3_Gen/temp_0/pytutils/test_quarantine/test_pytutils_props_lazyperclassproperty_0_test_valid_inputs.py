
import pytest
from pytutils.props import lazyperclassproperty

# Mocking a class property decorator if it's needed in the module
@pytest.fixture(autouse=True)
def mock_classproperty():
    from unittest.mock import MagicMock
    from functools import wraps

    def classproperty(func):
        @wraps(func)
        def get(cls):
            return func(cls)
        return property(get)

    # Replace the actual classproperty with our mock
    lazyperclassproperty.classproperty = MagicMock(side_effect=classproperty)

# Define a class with @lazyperclassproperty applied to a method that performs an expensive calculation
class ExpensiveClass:
    @lazyperclassproperty
    def cached_result(cls):
        return cls.__name__ + '_result'

def test_valid_inputs():
    # Test the first access, it should perform the calculation and cache the result
    assert ExpensiveClass.cached_result == 'ExpensiveClass_result'
    
    # Subsequent accesses should not re-run the expensive calculation
    class SubExpensiveClass(ExpensiveClass): pass
    assert SubExpensiveClass.cached_result == 'SubExpensiveClass_result'
    
    # Check that instances also have their own separate cache
    instance = ExpensiveClass()
    assert instance.cached_result == 'ExpensiveClass_result'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyperclassproperty_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_valid_inputs.py:23:4: E0213: Method 'cached_result' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_valid_inputs.py:24:15: E1101: Instance of 'ExpensiveClass' has no '__name__' member (no-member)


"""