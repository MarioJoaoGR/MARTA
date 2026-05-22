
import sys
from collections import OrderedDict
from httpie.utils import JsonDictPreservingDuplicateKeys

def test_edge_case_none():
    items = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
    json_dict = JsonDictPreservingDuplicateKeys(items)
    assert '__hack__' in json_dict and json_dict['__hack__'] == '__hack__'
