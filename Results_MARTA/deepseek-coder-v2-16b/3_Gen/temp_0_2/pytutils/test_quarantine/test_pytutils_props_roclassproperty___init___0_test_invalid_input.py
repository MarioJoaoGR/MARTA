
import pytest
from pytutils.props import roclassproperty

def test_invalid_input():
    with pytest.raises(TypeError):
        # Attempting to create an instance of roclassproperty without a callable function should raise a TypeError
        roclassproperty()  # This should fail because the constructor expects at least one argument (the callable)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_props_roclassproperty___init___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0_test_invalid_input.py:8:8: E1120: No value for argument 'f' in constructor call (no-value-for-parameter)


"""