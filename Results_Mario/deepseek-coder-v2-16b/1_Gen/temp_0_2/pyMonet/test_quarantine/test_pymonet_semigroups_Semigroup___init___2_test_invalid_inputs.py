
from pymonet.semigroups import Semigroup
import pytest

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # This should raise a TypeError because we are passing an extra argument
        Semigroup(5, 10)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Semigroup___init___2_test_invalid_inputs
pyMonet/Test4DT_tests/test_pymonet_semigroups_Semigroup___init___2_test_invalid_inputs.py:8:8: E1121: Too many positional arguments for constructor call (too-many-function-args)


"""