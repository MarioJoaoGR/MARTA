
import pytest
from pytutils.mappings import AttrDict

def test_valid_inputs():
    m = AttrDict(omg=True, whoa='yes')
    assert hasattr(m, 'omg'), "Instance of 'AttrDict' has no 'omg' member"
    assert hasattr(m, 'whoa'), "Instance of 'AttrDict' has no 'whoa' member"
    assert m.omg == True
    assert m.whoa == 'yes'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_AttrDict___init___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_mappings_AttrDict___init___0_test_valid_inputs.py:9:11: E1101: Instance of 'AttrDict' has no 'omg' member (no-member)
pytutils/Test4DT_tests/test_pytutils_mappings_AttrDict___init___0_test_valid_inputs.py:10:11: E1101: Instance of 'AttrDict' has no 'whoa' member (no-member)


"""