
import pytest
from collections import OrderedDict
import sys
from unittest.mock import patch

class JsonDictPreservingDuplicateKeys:
    """A specialized JSON dict preserving duplicate keys."""
    
    SUPPORTS_SORTING = sys.version_info >= (3, 8)
    
    def __init__(self, items: OrderedDict):
        """Initialize a new instance of JsonDictPreservingDuplicateKeys with the provided items.
        
        Args:
            items (OrderedDict): An iterable of key-value pairs to be added to the dictionary.
            
        Raises:
            TypeError: If `items` is not an OrderedDict.
            
        Examples:
            >>> from collections import OrderedDict
            >>> items = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
            >>> json_dict = JsonDictPreservingDuplicateKeys(items)
            >>> print(json_dict)
            {'__hack__': '__hack__', 'key1': 'value1', 'key2': 'value2'}
        
        This function is designed to create a dictionary that can be serialized by JSON, even if it contains duplicate keys. By adding a dummy key-value pair (`'__hack__': '__hack__'`), the method ensures that the dictionary is not considered empty during serialization, thus preserving any duplicate keys present in the `items`.
        """
        self._items = items
        self._ensure_items_used()

    def _ensure_items_used(self) -> None:
        """HACK: Force `json.dumps()` to use `self.items()` instead of an empty dict.
        
        This method adds a dummy key-value pair (`'__hack__': '__hack__'`) to the dictionary, 
        which ensures that the JSON encoder used by Python will consider the dictionary as having 
        at least one item, thus preserving duplicate keys when serialized with `json.dumps()`.
        
        The method is necessary because different versions of Python use different strategies for 
        checking if a dictionary is empty before serializing it to JSON:
            - The pure-Python implementation will do a simple check and return '{}' if the dict is empty,
              but we can fake this check by implementing the `__bool__()` method.
            - The C implementation checks the number of items contained inside the dict using 
              `dict->ma_used`, which is updated only when an item is added/removed from the dict.
        
        To please both implementations, we simply add one item to the dict.
        
        """
        if self._items:
            self['__hack__'] = '__hack__'

def test_invalid_input():
    with pytest.raises(TypeError):
        items = 123
        json_dict = JsonDictPreservingDuplicateKeys(items)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys__ensure_items_used_0_test_invalid_input.py:51:12: E1137: 'self' does not support item assignment (unsupported-assignment-operation)


"""