
import pytest
from pymonet.lazy import Lazy

def test_valid_input():
    def square(x):
        return x * x
    
    lazy = Lazy(square)
    validation = lazy.to_validation(5)
    
    assert isinstance(validation, Validation)
    assert validation.is_success()
    assert validation.get_value() == 25

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_lazy_Lazy_to_validation_0_test_valid_input
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_validation_0_test_valid_input.py:12:34: E0602: Undefined variable 'Validation' (undefined-variable)
pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_to_validation_0_test_valid_input.py:14:11: E1101: Instance of 'Validation' has no 'get_value' member (no-member)


"""