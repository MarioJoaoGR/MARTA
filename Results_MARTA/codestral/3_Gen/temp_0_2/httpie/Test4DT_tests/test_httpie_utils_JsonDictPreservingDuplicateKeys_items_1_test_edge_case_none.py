
import sys
from collections import OrderedDict
from httpie.utils import JsonDictPreservingDuplicateKeys, Items

def test_edge_case_none():
    items = OrderedDict([('a', 1), ('b', 2), ('a', 3)])
    jdpdk = JsonDictPreservingDuplicateKeys(items)
    
    assert jdpdk.items() == OrderedDict([('a', 1), ('b', 2), ('a', 3)])
