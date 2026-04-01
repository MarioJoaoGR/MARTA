
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_valid_input():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test setting via attribute style
    assert hasattr(b, 'whoa') == False  # Initially, 'whoa' should not be a direct attribute
    b.whoa = True
    assert hasattr(b, 'whoa') == True   # Now it should be an attribute
    assert b.whoa == True
    
    # Test setting via key-based indexing
    b['nice'] = False
    assert b['nice'] == False
    
    # Test recursion with nested attributes
    b.subdict = dict(test=True)
    assert hasattr(b, 'subdict') == True  # Check if subdict is an attribute
    assert isinstance(b.subdict, ProxyMutableAttrDict)  # Check if subdict is a ProxyMutableAttrDict instance
    assert b.subdict.test == True
    
    # Test setting nested attributes recursively
    b.nested = dict(inner=dict(value='hello'))
    assert hasattr(b, 'nested') == True  # Check if nested is an attribute
    assert isinstance(b.nested, ProxyMutableAttrDict)  # Check if nested is a ProxyMutableAttrDict instance
    assert hasattr(b.nested, 'inner') == True  # Check if inner is an attribute within nested
    assert b.nested.inner.value == 'hello'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___setattr___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___setattr___0_test_valid_input.py:23:11: E1101: Instance of 'dict' has no 'test' member (no-member)
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___setattr___0_test_valid_input.py:30:11: E1101: Instance of 'dict' has no 'inner' member (no-member)


"""