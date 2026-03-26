
import pytest
from pytutils.mappings import ProxyMutableAttrDict

def test_valid_inputs():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    
    assert isinstance(b, ProxyMutableAttrDict), "Instance should be of type ProxyMutableAttrDict"
    assert b.__mapping == a, "The proxied dictionary should match the input dictionary"
    assert b.whoa == True, "Attribute access should work correctly"
    assert b.hello == [1, 2, 3], "Attribute access should work correctly"
    assert b.why == 'always', "Attribute access should work correctly"
    
    # Adding a new key-value pair to check if it reflects in the dictionary
    b['new_key'] = 'new_value'
    assert b['new_key'] == 'new_value', "Setting via square bracket should work correctly"
    assert 'new_key' in b.__mapping, "The new key should be present in the proxied dictionary"
    
    # Setting an attribute that doesn't exist initially and checking if it gets added to the dictionary
    b.new_attr = 'new_value'
    assert b.new_attr == 'new_value', "Setting a non-existing attribute should add it to the proxied dictionary"
    assert 'new_attr' in b.__mapping, "The new attribute should be present in the proxied dictionary"
    
    # Checking if recursion works as expected
    b.subdict = dict(test=True)
    assert isinstance(b.subdict, ProxyMutableAttrDict), "Sub-dictionary should be of type ProxyMutableAttrDict"
    assert b.subdict.test == True, "Attribute access to sub-dictionary should work correctly"
    
    # Checking if the changes are reflected in the original dictionary
    c = dict(whoa=True, hello=[1,2,3], why='always')
    d = ProxyMutableAttrDict(c)
    assert d.whoa == True, "The proxied dictionary should reflect the initial state"
    
    # Adding a new key-value pair to check if it reflects in the original dictionary
    b['new_key'] = 'new_value'
    assert c == {'whoa': True, 'hello': [1, 2, 3], 'why': 'always', 'new_key': 'new_value'}, "The original dictionary should reflect changes made through the ProxyMutableAttrDict"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___init___0_test_valid_inputs.py:28:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""