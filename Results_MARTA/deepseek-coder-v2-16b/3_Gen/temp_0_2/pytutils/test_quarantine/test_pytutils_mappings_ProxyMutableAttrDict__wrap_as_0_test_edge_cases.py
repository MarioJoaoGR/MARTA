
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_edge_cases():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test setting new key-value pairs
    b['nice'] = False
    assert b['nice'] == False
    assert 'nice' in b
    
    # Test accessing existing keys via attribute and key
    b.whoa = 'yeee'
    assert b.whoa == 'yeee'
    assert b['whoa'] == 'yeee'
    
    # Test setting nested attributes recursively
    b.subdict = dict(test=True)
    assert b.subdict.test == True
    assert isinstance(b.subdict, ProxyMutableAttrDict)
    
    # Test accessing a non-existent key should raise AttributeError if recursion is enabled (default)
    with pytest.raises(AttributeError):
        getattr(b, 'non_existent_key')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_edge_cases.py:21:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""