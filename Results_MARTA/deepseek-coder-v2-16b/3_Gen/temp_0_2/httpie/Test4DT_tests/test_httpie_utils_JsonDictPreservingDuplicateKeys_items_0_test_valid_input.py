
import pytest
from httpie.utils import JsonDictPreservingDuplicateKeys
from collections import OrderedDict

def test_valid_input():
    items = OrderedDict([('a', 1), ('b', 2), ('a', 3)])
    jdpdk = JsonDictPreservingDuplicateKeys(items)
    assert jdpdk.items() == items
