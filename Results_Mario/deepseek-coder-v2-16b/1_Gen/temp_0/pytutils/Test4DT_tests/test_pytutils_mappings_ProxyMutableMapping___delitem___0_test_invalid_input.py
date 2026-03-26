
import pytest
from collections import UserDict

class ProxyMutableMapping:
    """
    Proxies access to an existing dict-like object, providing a view where items can be set and deleted just like in a regular dictionary.
    
    Parameters:
        mapping (collections.MutableMapping): A dict-like object to be wrapped by the proxy. This is the underlying data structure that the ProxyMutableMapping will act as a view of.
        fancy_repr (bool, optional): If True, the representation of the ProxyMutableMapping will include more detailed information about its contents. Defaults to True.
        dictify_repr (bool, optional): If True, the representation of the ProxyMutableMapping will be converted to a dictionary before being displayed. This is useful if you want to show all key-value pairs in a compact format. Defaults to False.
    
    Examples:
        >>> a = dict(whoa=True, hello=[1,2,3], why='always')
        >>> b = ProxyMutableMapping(a)
        
        To see the representation of the proxy object, you can use the following code:
        >>> print(b)  # This will show detailed information about the contents if fancy_repr is True, otherwise it will display a dictionary.
        
        Setting and deleting items works as expected:
        >>> b['nice'] = False
        >>> del b['whoa']
        
        To check that changes are being made to the underlying data structure, you can inspect the original dictionary:
        >>> print(a)  # The output will reflect any modifications made through the proxy.
    
    Significance within the broader context of the codebase:
    This class serves as a wrapper around a mutable mapping (such as a dictionary), allowing for controlled access and modification of its contents while providing flexibility in how the internal state is represented to users. It is particularly useful in scenarios where encapsulation and abstraction are desired, ensuring that external entities can interact with the data through a well-defined interface without direct access to the underlying implementation details.
    """
    def __init__(self, mapping, fancy_repr=True, dictify_repr=False):
        self.__fancy_repr = fancy_repr
        self.__dictify_repr = dictify_repr
        self._set_mapping(mapping)

    def _set_mapping(self, mapping):
        if not isinstance(mapping, (dict, UserDict)):
            raise TypeError("Mapping must be a dictionary-like object")
        self.__mapping = mapping if isinstance(mapping, dict) else dict(mapping)

    def __getitem__(self, key):
        return self.__mapping[key]

    def __setitem__(self, key, value):
        self.__mapping[key] = value

    def __delitem__(self, key):
        del self.__mapping[key]

    def __repr__(self):
        if self.__dictify_repr:
            return repr(self.__mapping)
        elif self.__fancy_repr:
            return f"<ProxyMutableMapping {{{', '.join(f'{k}: {v}' for k, v in self.__mapping.items())}}}>"
        else:
            return repr(self.__mapping)

def test_invalid_input():
    with pytest.raises(TypeError):
        a = 'not a mapping'
        ProxyMutableMapping(a)
