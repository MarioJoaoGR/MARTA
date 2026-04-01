
import pytest
from collections import UserDict

class HookableProxyMutableMapping(UserDict):
    def __init__(self, mapping, fancy_repr=True, dictify_repr=False):
        self.__mapping = mapping
        super().__init__(mapping)

    def __key_remove_prefix__(self, key):
        return key  # Default implementation does nothing

    def __key_allowed__(self, key) -> bool:
        return True  # By default, allow all keys

    def __iter__(self):
        orig_iter = super().__iter__()
        return (self.__key_remove_prefix__(key) for key in orig_iter if self.__key_allowed__(key))

class MyHookableMapping(HookableProxyMutableMapping):
    def __key_allowed__(self, key):
        return isinstance(key, int) or key == 'foo'

    def __key_remove_prefix__(self, key):
        return key  # Default implementation does nothing

def test_edge_cases():
    my_mapping = {'foo': 42}
    hookable_map = MyHookableMapping(my_mapping)

    # Test allowing specific keys and integers
    assert 'foo' in hookable_map
    with pytest.raises(KeyError):
        _ = hookable_map[1]

    # Test iteration with allowed keys only
    expected_keys = ['foo']
    actual_keys = list(hookable_map)
    assert sorted(actual_keys) == sorted(expected_keys)

    # Test setting and deleting items
    hookable_map['bar'] = 43
    assert 'bar' in hookable_map
    del hookable_map['bar']
    with pytest.raises(KeyError):
        _ = hookable_map['bar']

    # Test representation
    expected_repr = "{'foo': 42}"
    assert str(hookable_map) == expected_repr
