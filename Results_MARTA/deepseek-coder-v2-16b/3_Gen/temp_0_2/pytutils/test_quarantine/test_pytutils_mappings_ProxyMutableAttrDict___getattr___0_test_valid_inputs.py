
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_valid_inputs():
    a = dict(whoa=True, hello=[1, 2, 3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test setting new key-value pairs
    b['nice'] = False
    assert b['nice'] == False
    
    # Test attribute style access and modification
    b.whoa = 'yeee'
    assert b.whoa == 'yeee'
    
    # Test recursion with nested dictionaries
    b.subdict = dict(test=True)
    assert b.subdict.test == True
    
    # Test the custom repr
    expected_repr = "<ProxyMutableAttrDict {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False, 'state': 'new', 'subdict': <ProxyMutableAttrDict {'test': True}>}>"
    assert repr(b) == expected_repr

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___getattr___0_test_valid_inputs.py:19:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""