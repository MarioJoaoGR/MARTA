
import sys
from httpie.utils import JsonDictPreservingDuplicateKeys, Items
from collections import OrderedDict
import pytest

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or newer")
def test_edge_case_none():
    items = OrderedDict([('a', 1), ('b', 2), ('a', 3)])
    jdpdk = JsonDictPreservingDuplicateKeys(items)
    assert jdpdk.items() == OrderedDict([('a', 1), ('b', 2), ('a', 3)])
