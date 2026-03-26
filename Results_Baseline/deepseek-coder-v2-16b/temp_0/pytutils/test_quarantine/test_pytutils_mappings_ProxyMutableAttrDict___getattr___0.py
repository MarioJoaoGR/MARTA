
# Module: pytutils.mappings
import pytest
from pytutils.mappings import ProxyMutableAttrDict
import collections

# Test initialization with a dictionary
def test_init_with_dict():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    assert isinstance(b, ProxyMutableAttrDict)
    assert b == {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}

# Test customizing representation with fancy_repr and dictify_repr
def test_custom_representation():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a, fancy_repr=False, dictify_repr=True)
    assert repr(b) == "<ProxyMutableAttrDict {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>"

# Test disabling recursion for nested structures
def test_disable_recursion():
    a = dict(whoa=True, hello=[1,2,3], why='always', subdict=dict(test=True))
    b = ProxyMutableAttrDict(a, recursion=False)
    with pytest.raises(AttributeError):
        _ = b.subdict.test  # This should raise an AttributeError because recursion is disabled

# Test setting attributes dynamically
def test_set_attributes():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    b['nice'] = False
    assert b['nice'] == False
    b.whoa = 'yeee'
    assert b.whoa == 'yeee'

# Test accessing nested structures recursively
def test_nested_recursion():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    b.subdict = dict(test=True)
    assert b.subdict.test == True

# Test using ProxyMutableAttrDict with different parameters
def test_different_parameters():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a, fancy_repr=False, recursion=True)
    assert repr(b) == "<ProxyMutableAttrDict {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___getattr___0
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___getattr___0.py:25:12: E1101: Instance of 'dict' has no 'test' member (no-member)
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___getattr___0.py:41:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""