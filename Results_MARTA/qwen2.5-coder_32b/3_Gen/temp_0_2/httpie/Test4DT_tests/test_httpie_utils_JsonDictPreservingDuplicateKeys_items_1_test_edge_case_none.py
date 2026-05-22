
import sys
from collections import OrderedDict
from httpie.utils import JsonDictPreservingDuplicateKeys, Items

class TestJsonDictPreservingDuplicateKeys:
    def test_edge_case_none(self):
        items = OrderedDict([('a', 1), ('b', 2), ('a', 3)])
        jdpdk = JsonDictPreservingDuplicateKeys(items)
        
        assert jdpdk.items() == OrderedDict([('a', 1), ('b', 2), ('a', 3)])
