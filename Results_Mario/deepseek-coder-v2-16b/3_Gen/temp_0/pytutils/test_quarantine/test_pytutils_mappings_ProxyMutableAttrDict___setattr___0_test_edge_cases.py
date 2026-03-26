
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_setattr():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Setting attribute directly
    b.state = 'new'
    assert b['state'] == 'new', "Failed to set attribute through __setattr__"
    
    # Setting nested attribute
    b.subdict = dict(test=True)
    assert isinstance(b.subdict, ProxyMutableAttrDict), "Failed to create nested ProxyMutableAttrDict instance"
    assert b.subdict.test == True, "Nested attribute not set correctly"
    
    # Setting existing key should raise an error if recursion is disabled
    with pytest.raises(AttributeError):
        b.whoa = 'new_value'  # This should raise AttributeError because whoa is already a key in the dictionary

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___setattr___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___setattr___0_test_edge_cases.py:16:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""