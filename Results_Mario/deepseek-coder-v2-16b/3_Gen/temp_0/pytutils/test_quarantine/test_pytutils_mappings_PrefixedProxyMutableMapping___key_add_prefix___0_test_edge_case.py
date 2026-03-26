
import pytest
from pytutils.mappings import PrefixedProxyMutableMapping
from collections import OrderedDict

def test_prefixed_proxy_mutable_mapping():
    # Create an instance of PrefixedProxyMutableMapping with a prefix and a mapping
    my_dict = {'foo': 1, 'bar': 2}
    prefixed_mapping = PrefixedProxyMutableMapping('pre_', my_dict)
    
    # Test adding a new key with the prefix
    prefixed_mapping['new_key'] = 3
    assert 'pre_new_key' in prefixed_mapping.keys()
    assert prefixed_mapping['pre_new_key'] == 3
    
    # Test accessing an existing key with the prefix
    assert prefixed_mapping['pre_foo'] == 1
    
    # Test removing a key with the prefix
    removed_value = prefixed_mapping.pop('pre_foo')
    assert removed_value == 1
    assert 'pre_foo' not in prefixed_mapping
    
    # Test initialization with only_prefixed set to False
    prefixed_proxy = PrefixedProxyMutableMapping('pre_', my_dict, only_prefixed=False)
    prefixed_proxy['key3'] = 4
    assert 'key3' in prefixed_proxy
    assert prefixed_proxy['key3'] == 4
    
    # Test the repr method for both cases
    assert str(prefixed_mapping) == "{'pre_foo': 1, 'pre_bar': 2, 'pre_new_key': 3}"
    assert str(prefixed_proxy) == "{'pre_foo': 1, 'pre_bar': 2, 'key3': 4}"

# Run the test function
if __name__ == "__main__":
    pytest.main()

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
pytutils/Test4DT_tests/test_pytutils_mappings_PrefixedProxyMutableMapping___key_add_prefix___0_test_edge_case.py:3: in <module>
    from pytutils.mappings import PrefixedProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-76pzlrmd'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-gjgrjde_'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-2lbvj5yl'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev - AttributeError: module 'collections' has no attribute 'M...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 3 warnings, 1 error in 0.13s =========================
"""