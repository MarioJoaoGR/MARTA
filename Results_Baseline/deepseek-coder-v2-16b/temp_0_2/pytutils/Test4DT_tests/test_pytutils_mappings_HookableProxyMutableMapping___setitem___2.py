
import pytest
from collections import UserDict

class HookableProxyMutableMapping(UserDict):
    def __init__(self, mapping, fancy_repr=True, dictify_repr=False):
        self.__mapping = mapping
        super().__init__(mapping)

    def __key_trans__(self, key, store=False, get=False, contains=False, delete=False):
        return key  # Placeholder for potential custom transformations

    def __setitem__(self, item, value):
        item = self.__key_trans__(item, store=True)
        super().__setitem__(item, value)

# Test initialization with default parameters
def test_init_default():
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    hookable_proxy = HookableProxyMutableMapping(my_dict)
    assert isinstance(hookable_proxy, HookableProxyMutableMapping)
    assert hookable_proxy.data == my_dict

# Test initialization with custom fancy_repr and dictify_repr parameters
def test_init_custom_params():
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    hookable_proxy = HookableProxyMutableMapping(my_dict, fancy_repr=True, dictify_repr=False)
    assert isinstance(hookable_proxy, HookableProxyMutableMapping)
    assert hookable_proxy.data == my_dict

# Test setting a new item in the mapping
def test_setitem():
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    hookable_proxy = HookableProxyMutableMapping(my_dict)
    hookable_proxy['key3'] = 'value3'
    assert hookable_proxy.data == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Test setting a new item with custom key transformation
class MyHookableMapping(HookableProxyMutableMapping):
    def __key_trans__(self, key, store=False, get=False, contains=False, delete=False):
        return f"custom_{key}" if store else key

def test_setitem_with_custom_transformation():
    my_dict = {'a': 1, 'b': 2}
    hookable_mapping = MyHookableMapping(my_dict)
    assert hookable_mapping['custom_a'] == 1
    hookable_mapping['c'] = 3

# Test setting an item with a custom key transformation that changes the key
def test_setitem_with_key_transformation():
    my_dict = {}
    hookable_proxy = HookableProxyMutableMapping(my_dict)
    hookable_proxy['some_key'] = 'value'
    assert hookable_proxy.data == {'some_key': 'value'}  # Ensure the key is transformed correctly

# Test setting an item with a custom key transformation that changes the key and ensures it updates the data dictionary
def test_setitem_with_key_transformation_updates_data():
    my_dict = {}
    hookable_proxy = HookableProxyMutableMapping(my_dict)
    hookable_proxy['some_key'] = 'value'
    assert hookable_proxy.data == {'some_key': 'value'}  # Ensure the key is transformed correctly and data dictionary is updated

# Test setting an item with a custom key transformation that changes the key and ensures it updates the data dictionary using subclass
class MyHookableMappingWithTransformation(HookableProxyMutableMapping):
    def __key_trans__(self, key, store=False, get=False, contains=False, delete=False):
        return f"custom_{key}" if store else key

def test_setitem_with_key_transformation_updates_data_subclass():
    my_dict = {}
    hookable_proxy = MyHookableMappingWithTransformation(my_dict)
    hookable_proxy['some_key'] = 'value'
    assert hookable_proxy.data == {'custom_some_key': 'value'}  # Ensure the key is transformed correctly and data dictionary is updated using subclass
