
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_edge_cases():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test attribute access to existing key
    assert b.whoa == True
    
    # Test setting new attribute
    b.state = 'new'
    assert b.state == 'new'
    
    # Test accessing nested attributes
    b.subdict = dict(test=True)
    assert b.subdict.test == True
    
    # Test non-existing key should raise AttributeError
    with pytest.raises(AttributeError):
        getattr(b, 'nonexistentkey')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_edge_cases.py:18:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""