
# Module: pytutils.mappings
import pytest
from pytutils.mappings import ProxyMutableAttrDict

# Test initialization with a dictionary
def test_init_with_dict():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    assert isinstance(b, ProxyMutableAttrDict)
    assert b.__mapping == a

# Test attribute-style access
def test_attribute_style_access():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    assert b.whoa == True
    assert b.hello == [1, 2, 3]
    assert b.why == 'always'

# Test setting new key-value pairs
def test_setting_new_key_value_pairs():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    b['nice'] = False
    assert b['nice'] == False
    b['whoa'] = 'yeee'
    assert b['whoa'] == 'yeee'

# Test checking that changes are reflected in the underlying mapping
def test_changes_reflected():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    b['nice'] = False
    assert a == {'whoa': True, 'hello': [1, 2, 3], 'why': 'always', 'nice': False}

# Test handling nested dictionaries recursively
def test_recursive_handling():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    b.subdict = dict(test=True)
    assert isinstance(b.subdict, ProxyMutableAttrDict)
    assert b.subdict.test == True

# Test attribute error for non-existent attributes
def test_attribute_error():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableAttrDict(a)
    with pytest.raises(AttributeError):
        assert b.non_existent_attr

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableAttrDict___getattr___0
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableAttrDict___getattr___0.py:43:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""