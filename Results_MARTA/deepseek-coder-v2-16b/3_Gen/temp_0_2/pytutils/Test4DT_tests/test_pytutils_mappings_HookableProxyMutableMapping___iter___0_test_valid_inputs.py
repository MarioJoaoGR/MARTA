
import pytest
from collections import UserDict

class HookableProxyMutableMapping(UserDict):
    def __init__(self, mapping, fancy_repr=True, dictify_repr=False):
        self.__mapping = mapping
        super().__init__(mapping)

    def __key_remove_prefix__(self, key):
        return key  # Default implementation does nothing

    def __key_allowed__(self, key) -> bool:
        return True

    def __iter__(self):
        orig_iter = super().__iter__()
        return (self.__key_remove_prefix__(key) for key in orig_iter if self.__key_allowed__(key))

class MyHookableMapping(HookableProxyMutableMapping):
    def __key_allowed__(self, key):
        return isinstance(key, int) or key == 'foo'

    def __key_remove_prefix__(self, key):
        return key  # Default implementation does nothing

def test_valid_inputs():
    my_mapping = {'foo': 42}
    hookable_map = MyHookableMapping(my_mapping)

    assert 'foo' in hookable_map
    assert list(hookable_map.keys()) == ['foo']
    assert list(hookable_map.values()) == [42]
    assert list(hookable_map.items()) == [('foo', 42)]

    with pytest.raises(KeyError):
        hookable_map[1]
