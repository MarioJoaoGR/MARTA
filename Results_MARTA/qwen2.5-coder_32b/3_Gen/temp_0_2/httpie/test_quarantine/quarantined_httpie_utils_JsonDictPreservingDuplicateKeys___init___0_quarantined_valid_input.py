
import pytest
from unittest.mock import patch
from httpie.utils import sys

class JsonDictPreservingDuplicateKeys:
    """A specialized JSON dict preserving duplicate keys."""
    
    SUPPORTS_SORTING = sys.version_info >= (3, 8)
    
    def __init__(self, items: Items):
        """Initialize a new instance of JsonDictPreservingDuplicateKeys with the provided items.
        
        Args:
            items (Items): An iterable of key-value pairs to be added to the dictionary.
            
        Raises:
            TypeError: If `items` is not an iterable.
            
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

def test_valid_input():
    from collections import OrderedDict
    
    with patch('httpie.utils.sys') as mock_sys:
        # Mocking sys.version_info to return a version >= 3.8 for testing purposes
        mock_sys.version_info = (3, 8)  # This is a tuple representing the Python version

        items = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
        json_dict = JsonDictPreservingDuplicateKeys(items)

        assert '__hack__' in json_dict, "Expected '__hack__' key to be present in the dictionary."
        assert len(json_dict) == 3, "Expected the dictionary to have exactly three items after initialization."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_utils_JsonDictPreservingDuplicateKeys___init___0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_JsonDictPreservingDuplicateKeys___init___0_test_valid_input.py:11:30: E0602: Undefined variable 'Items' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_JsonDictPreservingDuplicateKeys___init___0_test_valid_input.py:50:12: E1137: 'self' does not support item assignment (unsupported-assignment-operation)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_utils_JsonDictPreservingDuplicateKeys___init___0_test_valid_input.py:62:29: E1135: Value 'json_dict' doesn't support membership test (unsupported-membership-test)


"""