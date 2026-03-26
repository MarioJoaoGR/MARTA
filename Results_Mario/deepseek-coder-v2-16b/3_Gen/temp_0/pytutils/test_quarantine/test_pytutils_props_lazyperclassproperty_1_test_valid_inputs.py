
import pytest
from pytutils.props import lazyperclassproperty

# Mocking ExpensiveClass for testing purposes
@pytest.fixture(name="ExpensiveClass")
def fixture_expensive_class():
    class ExpensiveClass:
        def __init__(self, value):
            self.value = value
        
        @lazyperclassproperty
        def cached_result(cls):
            return cls.__name__ + '_result'
    
    return ExpensiveClass

def test_valid_inputs(ExpensiveClass):
    # Create an instance of the mocked class
    expensive_instance = ExpensiveClass("test")
    
    # Check that the property is calculated correctly and only once per class/inheritor
    assert expensive_instance.cached_result == "ExpensiveClass_result"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyperclassproperty_1_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_1_test_valid_inputs.py:13:8: E0213: Method 'cached_result' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_1_test_valid_inputs.py:14:19: E1101: Instance of 'ExpensiveClass' has no '__name__' member (no-member)


"""