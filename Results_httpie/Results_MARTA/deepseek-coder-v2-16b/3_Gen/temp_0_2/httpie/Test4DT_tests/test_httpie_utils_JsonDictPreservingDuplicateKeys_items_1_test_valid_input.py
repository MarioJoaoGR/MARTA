
import sys
from collections import OrderedDict
from httpie.utils import JsonDictPreservingDuplicateKeys

def test_valid_input():
    items = OrderedDict([('a', 1), ('b', 2), ('a', 3)])
    json_dict = JsonDictPreservingDuplicateKeys(items)
    
    assert isinstance(json_dict, JsonDictPreservingDuplicateKeys)
    assert json_dict.items() == items
