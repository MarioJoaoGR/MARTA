
import pytest
from pymonets.semigroups import Max

def test_error_case():
    with pytest.raises(TypeError):
        invalid_max = Max('string')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_semigroups_Max_concat_2_test_error_case
pyMonet/Test4DT_tests/test_pymonet_semigroups_Max_concat_2_test_error_case.py:3:0: E0401: Unable to import 'pymonets.semigroups' (import-error)


"""