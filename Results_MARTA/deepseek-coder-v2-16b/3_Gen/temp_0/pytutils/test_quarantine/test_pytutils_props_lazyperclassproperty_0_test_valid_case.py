
from pytutils.props import lazyperclassproperty

class MyClass:
    @lazyperclassproperty
    def cached_result(cls):
        return cls.__name__ + '_result'

# Example usage in a test case
def test_valid_case():
    class SubClass(MyClass):
        pass
    
    # First access should compute the result
    assert MyClass().cached_result == 'MyClass_result'
    
    # Subsequent accesses should return the cached result
    assert MyClass().cached_result == 'MyClass_result'
    assert SubClass().cached_result == 'SubClass_result'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_lazyperclassproperty_0_test_valid_case
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_valid_case.py:6:4: E0213: Method 'cached_result' should have "self" as first argument (no-self-argument)
pytutils/Test4DT_tests/test_pytutils_props_lazyperclassproperty_0_test_valid_case.py:7:15: E1101: Instance of 'MyClass' has no '__name__' member (no-member)


"""