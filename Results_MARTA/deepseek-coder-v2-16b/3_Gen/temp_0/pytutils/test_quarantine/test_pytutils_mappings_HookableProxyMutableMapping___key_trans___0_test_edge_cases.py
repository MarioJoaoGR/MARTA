
import pytest
from pytutils.mappings import HookableProxyMutableMapping

def test_edge_cases():
    # Create a mock mapping for testing
    class MockMapping(dict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
        def __getitem__(self, key):
            return f"get_{key}"
        
        def __setitem__(self, key, value):
            return f"set_{key}_{value}"
        
        def __contains__(self, key):
            return f"contains_{key}"
        
        def __delitem__(self, key):
            return f"delete_{key}"
    
    mock_mapping = MockMapping({'key1': 'value1', 'key2': 'value2'})
    proxy_map = HookableProxyMutableMapping(mock_mapping)

    # Test get item transformation
    assert proxy_map.__getitem__('key1') == "get_key1"
    
    # Test set item transformation
    proxy_map['new_key'] = 'new_value'
    assert proxy_map['new_key'] == "set_new_key_new_value"
    
    # Test contains check transformation
    assert ('key1' in proxy_map) == "contains_key1"
    
    # Test delete item transformation
    del proxy_map['key2']
    assert not 'key2' in proxy_map

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
________________________ ERROR collecting test session _________________________
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_trans___0_test_edge_cases.py:3: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-0sp2sh1v'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-_6oieyue'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-5lzoi2b4'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev - AttributeError: module 'collections' has no attribute 'M...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 3 warnings, 1 error in 0.16s =========================
"""