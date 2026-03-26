
import pytest
from collections import UserDict

class HookableProxyMutableMapping(UserDict):
    def __init__(self, mapping, fancy_repr=True, dictify_repr=False):
        self.__mapping = mapping
        super().__init__(mapping)

    def __key_trans__(self, key, store=False, get=False, contains=False, delete=False):
        return key

    def __setitem__(self, item, value):
        item = self.__key_trans__(item, store=True)
        super().__setitem__(item, value)

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)
        raise KeyError(key)

    def __contains__(self, item):
        item = self.__key_trans__(item, contains=True)
        return super().__contains__(item)

# Test case for setting a new item in the mapping with default behavior
def test_setitem_default():
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    hookable_proxy = HookableProxyMutableMapping(my_dict)
    hookable_proxy['key3'] = 'value3'
    assert hookable_proxy.data == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Test case for setting a new item with custom key transformation
class MyHookableMapping(HookableProxyMutableMapping):
    def __key_trans__(self, key, store=False, get=False, contains=False, delete=False):
        return f"custom_{key}" if store else key

def test_setitem_with_custom_transformation():
    my_dict = {'a': 1, 'b': 2}
    hookable_mapping = MyHookableMapping(my_dict)
    assert hookable_mapping['custom_a'] == 1
    hookable_mapping['c'] = 3
    assert hookable_mapping.data == {'custom_a': 1, 'custom_b': 2, 'custom_c': 3}

# Test case for setting a new item with custom key transformation and ensuring the original mapping is not affected
def test_setitem_with_custom_transformation_isolated():
    my_dict = {'original_key': 'value'}
    hookable_mapping = MyHookableMapping(my_dict)