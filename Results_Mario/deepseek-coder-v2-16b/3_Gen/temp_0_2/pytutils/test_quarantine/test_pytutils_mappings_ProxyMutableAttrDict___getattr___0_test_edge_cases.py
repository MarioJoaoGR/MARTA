
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_edge_cases():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test accessing existing key
    assert b.whoa == True
    
    # Test setting new attribute
    b.state = 'new'
    assert hasattr(b, 'state')
    assert b.state == 'new'
    
    # Test accessing non-existing key with recursion enabled
    with pytest.raises(AttributeError):
        b.non_existent_key
    
    # Test setting nested attribute
    b.subdict = dict(test=True)
    assert hasattr(b, 'subdict')
    assert b.subdict.test == True
    
    # Test accessing existing key in nested structure
    assert b.subdict.test == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_edge_cases.py:24:11: E1101: Instance of 'dict' has no 'test' member (no-member)
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_edge_cases.py:27:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""