
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty

# Test case to check the initialization of rwclassproperty with invalid input
def test_invalid_input():
    # Define a function that raises an error when used as a property setter
    def invalid_prop(cls, value):
        raise ValueError("Invalid operation")
    
    # Attempt to initialize rwclassproperty with the invalid function
    with pytest.raises(TypeError) as excinfo:
        class InvalidClass(metaclass=rwclassproperty.meta):
            @rwclassproperty(lambda cls: 123, fset=invalid_prop)
            def foo(cls):
                pass
    
    # Check that the error message contains the expected text
    assert "Getter or setter must be a function" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty__fix_function_0_test_invalid_input.py:15:12: E0213: Method 'foo' should have "self" as first argument (no-self-argument)


"""