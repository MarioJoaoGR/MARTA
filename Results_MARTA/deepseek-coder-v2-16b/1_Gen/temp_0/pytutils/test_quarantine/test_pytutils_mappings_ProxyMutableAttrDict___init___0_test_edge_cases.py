
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_edge_cases():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test setting and getting values through key-based syntax
    assert 'whoa' in b
    assert b['whoa'] == True
    b['nice'] = False
    assert b['nice'] == False
    
    # Test attribute-style access
    assert hasattr(b, 'whoa')
    assert b.whoa == True
    b.state = 'new'
    assert hasattr(b, 'state')
    assert b.state == 'new'
    
    # Test recursion with nested attributes
    b.subdict = dict(test=True)
    assert hasattr(b, 'subdict')
    assert b.subdict.test == True
    
    # Check that the changes are reflected in the underlying mapping
    assert a['nice'] == False
    assert a['whoa'] == True
    assert 'state' not in a
    assert 'subdict' not in a

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_edge_cases.py:25:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""