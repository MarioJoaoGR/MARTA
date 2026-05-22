
import pytest
from collections import OrderedDict
import sys

class JsonDictPreservingDuplicateKeys:
    """A specialized JSON dict preserving duplicate keys."""
    
    SUPPORTS_SORTING = sys.version_info >= (3, 8)
    
    def __init__(self, items: OrderedDict):
        self._items = items
        self._ensure_items_used()

    def _ensure_items_used(self) -> None:
        if self._items:
            self['__hack__'] = '__hack__'
    
    def __getitem__(self, key):
        return self._items[key]
    
    def __setitem__(self, key, value):
        self._items[key] = value
    
    def items(self) -> OrderedDict:
        """Return all items, duplicate ones included."""
        return self._items

def test_valid_input():
    items = OrderedDict([('a', 1), ('b', 2), ('a', 3)])
    jdpdk = JsonDictPreservingDuplicateKeys(items)
    assert jdpdk.items() == OrderedDict([('a', 1), ('b', 2), ('a', 3)])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys_items_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        items = OrderedDict([('a', 1), ('b', 2), ('a', 3)])
        jdpdk = JsonDictPreservingDuplicateKeys(items)
>       assert jdpdk.items() == OrderedDict([('a', 1), ('b', 2), ('a', 3)])
E       AssertionError: assert OrderedDict([... '__hack__')]) == OrderedDict([...3), ('b', 2)])
E         
E         Omitting 2 identical items, use -vv to show
E         Left contains 1 more item:
E         {'__hack__': '__hack__'}
E         Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys_items_0_test_valid_input.py:32: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_utils_JsonDictPreservingDuplicateKeys_items_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""