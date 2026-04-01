
from pytutils.lazy.lazy_import import ScopeReplacer, disallow_proxying
import pytest

def test_invalid_input():
    # Arrange
    invalid_object = "not a ScopeReplacer"
    
    # Act and Assert
    with pytest.raises(TypeError):
        disallow_proxying(invalid_object)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_disallow_proxying_2_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_disallow_proxying_2_test_invalid_input.py:11:8: E1121: Too many positional arguments for function call (too-many-function-args)


"""