
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_edge_cases():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test accessing existing key as attribute
    assert b.whoa == True
    
    # Test setting new attribute
    b.state = 'new'
    assert hasattr(b, 'state')
    assert b.state == 'new'
    
    # Test accessing nested dictionary as attribute
    b.subdict = dict(test=True)
    assert b.subdict.test == True
    
    # Test setting new key in nested dictionary
    b.subdict['new_key'] = False
    assert b.subdict['new_key'] == False
    
    # Test accessing non-existing attribute should raise AttributeError
    with pytest.raises(AttributeError):
        b.non_existent_attribute

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_edge_cases.py:19:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""