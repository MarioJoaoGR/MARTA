
import pytest
from collections import OrderedDict
from httpie.utils import JsonDictPreservingDuplicateKeys

def test_valid_input():
    items = OrderedDict([('a', 1), ('b', 2), ('a', 3)])
    jdpdk = JsonDictPreservingDuplicateKeys(items)
    assert jdpdk.items() == OrderedDict([('a', 1), ('b', 2), ('a', 3)])
