
# Module: pytutils.mappings
import pytest
from pytutils.mappings import ProxyMutableMapping

# Test initialization with a dictionary
def test_init_with_dict():
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    proxy_mapping = ProxyMutableMapping(my_dict)
    assert len(proxy_mapping) == 2, "Initialization with a dictionary should set the length to 2"
    assert list(proxy_mapping.keys()) == ['key1', 'key2'], "Keys should match the initialized dictionary"

# Test attribute-style access
def test_attribute_style_access():
    proxy_mapping = ProxyMutableMapping({'whoa': True, 'hello': [1, 2, 3], 'why': 'always'})
    assert proxy_mapping.whoa == True, "Attribute access should return the value of 'whoa'"
    with pytest.raises(AttributeError):
        _ = proxy_mapping.nonexistentkey  # Ensure accessing a non-existent attribute raises an AttributeError

# Test setting a new key-value pair
def test_setting_new_item():
    proxy_mapping = ProxyMutableMapping({'whoa': True, 'hello': [1, 2, 3], 'why': 'always'})
    proxy_mapping['nice'] = False
    assert len(proxy_mapping) == 4, "Setting a new key-value pair should increase the length"
    assert list(proxy_mapping.keys()) == ['whoa', 'hello', 'why', 'nice'], "Keys should include the newly added key"

# Test setting nested dictionary recursively
def test_nested_dict():
    proxy_mapping = ProxyMutableMapping({'whoa': True, 'hello': [1, 2, 3], 'why': 'always'})
    proxy_mapping.subdict = {'test': True}
    assert len(proxy_mapping) == 4, "Setting a nested dictionary should increase the length"
    assert list(proxy_mapping.keys()) == ['whoa', 'hello', 'why', 'subdict'], "Keys should include the newly added subdict key"
    assert proxy_mapping.subdict.test == True, "Nested attribute access should return the value of 'test'"

# Test using fancy_repr and dictify_repr parameters
def test_fancy_and_dictify_repr():
    my_dict = {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}
    proxy_mapping = ProxyMutableMapping(my_dict, fancy_repr=True, dictify_repr=False)
    assert str(proxy_mapping) == "<ProxyMutableAttrDict {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>", "fancy_repr should provide a detailed representation"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_ProxyMutableMapping___len___0
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping___len___0.py:33:11: E1101: Instance of 'dict' has no 'test' member (no-member)


"""