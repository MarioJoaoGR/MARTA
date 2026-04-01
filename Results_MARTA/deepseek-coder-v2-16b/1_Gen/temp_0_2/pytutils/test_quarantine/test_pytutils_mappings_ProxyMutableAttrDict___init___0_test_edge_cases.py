
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_edge_cases():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    assert isinstance(b, ProxyMutableAttrDict)
    assert b.__mapping == a
    assert b.whoa == True
    assert b['hello'] == [1, 2, 3]
    
    b['nice'] = False
    assert b['nice'] == False
    
    b.whoa = 'yeee'
    assert b.whoa == 'yeee'
    
    a_copy = a.copy()
    a_copy['nice'] = False
    a_copy['whoa'] = 'yeee'
    assert a == a_copy
    
    b.state = 'new'
    assert b.state == 'new'
    
    b.subdict = dict(test=True)
    assert b.subdict.test == True
    
    repr_str = "<ProxyMutableAttrDict {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False, 'state': 'new', 'subdict': <ProxyMutableAttrDict {'test': True}>}>"
    assert repr(b) == repr_str

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_edge_cases.py:29:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""