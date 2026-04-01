
import pytest
from pytutils.ext.rwclassproperty import rwclassproperty

def test_invalid_inputs():
    # Test that attempting to use @rwclassproperty without a classmethod or staticmethod raises an AttributeError
    with pytest.raises(AttributeError):
        class Z:
            @rwclassproperty
            def foo(cls):
                return 123
    
    # The above code should raise an AttributeError because the property is not defined as a class method or static method.

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_ext_rwclassproperty_rwclassproperty_setter_0_test_invalid_inputs.py:10:12: E0213: Method 'foo' should have "self" as first argument (no-self-argument)


"""