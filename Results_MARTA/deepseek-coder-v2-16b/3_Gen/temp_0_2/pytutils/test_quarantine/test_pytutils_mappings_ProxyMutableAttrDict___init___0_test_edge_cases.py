
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_edge_cases():
    a = dict(whoa=True, hello=[1, 2, 3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test initial state
    assert isinstance(b, ProxyMutableAttrDict)
    assert b == {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}
    
    # Test setting new key-value pairs
    b['nice'] = False
    assert b['nice'] == False
    assert b == {'whoa': True, 'hello': [1, 2, 3], 'why': 'always', 'nice': False}
    
    # Test attribute style access and setting
    b.whoa = 'yeee'
    assert b.whoa == 'yeee'
    assert b == {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False}
    
    # Test recursion
    b.subdict = dict(test=True)
    assert isinstance(b.subdict, ProxyMutableAttrDict)
    assert b.subdict.test == True
    assert b == {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False, 'subdict': {'test': True}}
    
    # Test setting nested attributes recursively
    b.nested_subdict = dict(inner=dict(value='nested'))
    assert isinstance(b.nested_subdict, ProxyMutableAttrDict)
    assert b.nested_subdict.inner.value == 'nested'
    assert b == {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False, 'subdict': {'test': True}, 'nested_subdict': {'inner': {'value': 'nested'}}}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_edge_cases.py:26:11: E1101: Instance of 'dict' has no 'test' member (no-member)
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_edge_cases.py:32:11: E1101: Instance of 'dict' has no 'inner' member (no-member)


"""