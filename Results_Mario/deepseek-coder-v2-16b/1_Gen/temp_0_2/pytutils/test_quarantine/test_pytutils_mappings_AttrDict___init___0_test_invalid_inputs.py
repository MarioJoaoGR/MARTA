
import pytest
from pytutils.mappings import AttrDict

def test_invalid_inputs():
    with pytest.raises(AttributeError):
        m = AttrDict()
        m.non_existent_attribute  # This should raise an AttributeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_AttrDict___init___0_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_mappings_AttrDict___init___0_test_invalid_inputs.py:8:8: E1101: Instance of 'AttrDict' has no 'non_existent_attribute' member (no-member)


"""