
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_valid_inputs():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    # Test setting and getting values via key-based syntax
    assert 'whoa' not in dir(b), "Attribute access should not be allowed directly"
    b['nice'] = False
    assert b['nice'] == False, "Setting a value via key-based syntax failed"
    
    # Test setting and getting values via attribute-style syntax
    assert 'whoa' in dir(b), "Attribute access should be allowed for existing keys"
    b.whoa = 'yeee'
    assert b['whoa'] == 'yeee', "Setting a value via attribute-style syntax failed"
    
    # Test setting new attributes recursively
    b.subdict = dict(test=True)
    assert isinstance(b.subdict, ProxyMutableAttrDict), "Recursive attribute access should work for nested dictionaries"
    assert b.subdict.test == True, "Accessing a value within the nested dictionary failed"
    
    # Test modification of existing attributes
    b.whoa = 'new_value'
    assert b['whoa'] == 'new_value', "Modifying an existing attribute via key-based syntax failed"
    b.whoa = 'yet_another_value'
    assert b.whoa == 'yet_another_value', "Modifying an existing attribute via attribute-style syntax failed"
    
    # Test that the changes are reflected in the underlying dictionary
    assert a['whoa'] == 'yet_another_value', "Changes to the ProxyMutableAttrDict should be reflected in the underlying dictionary"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict__wrap_as_0_test_valid_inputs.py:22:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""