
# Module: pytutils.mappings
import pytest
from pytutils.mappings import ProxyMutableAttrDict
import collections

# Example 1: Basic Initialization
def test_basic_initialization():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    assert str(b) == "<ProxyMutableAttrDict {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>"

# Example 2: Setting and Getting Values
def test_setting_and_getting_values():
    a = dict()
    b = ProxyMutableAttrDict(a)
    b['nice'] = False
    b.whoa = 'yeee'
    assert str(b) == "<ProxyMutableAttrDict {'nice': False, 'whoa': 'yeee'}>"
    assert b.whoa == 'yeee'

# Example 3: Recursive Attribute Setting
def test_recursive_attribute_setting():
    a = dict()
    b = ProxyMutableAttrDict(a)
    b.subdict = dict(test=True)
    assert str(b) == "<ProxyMutableAttrDict {'subdict': <ProxyMutableAttrDict {'test': True}>}>"
    assert b.subdict.test is True

# Example 4: Customizing Representation
def test_customizing_representation():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a, fancy_repr=False, dictify_repr=True)
    assert str(b) == "<ProxyMutableAttrDict {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>"

# Example 5: Disabling Recursion
def test_disabling_recursion():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a, recursion=False)
    with pytest.raises(AttributeError):
        b.subdict = dict(test=True)

# Additional Test Cases for __setattr__ method
def test_setattr():
    a = dict()
    b = ProxyMutableAttrDict(a)
    b.new_key = 'value'
    assert str(b) == "<ProxyMutableAttrDict {'new_key': 'value'}>"
    with pytest.raises(AttributeError):
        b.non_existing_key = 'value'  # This should raise an AttributeError

def test_setattr_with_nested():
    a = dict()
    b = ProxyMutableAttrDict(a)
    b.nested = {'test': True}
    assert str(b) == "<ProxyMutableAttrDict {'nested': <ProxyMutableAttrDict {'test': True}>}>"
    assert b.nested.test is True

def test_setattr_with_non_mapping():
    a = dict()
    b = ProxyMutableAttrDict(a)
    with pytest.raises(AttributeError):
        b.non_mapping_key = 123  # This should raise an AttributeError because it's not a mapping

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___setattr___0
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___setattr___0.py:28:11: E1101: Instance of 'dict' has no 'test' member (no-member)
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___setattr___0.py:57:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""