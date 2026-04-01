
# Importing the necessary classes from pytutils.mappings
from pytutils.mappings import HookableProxyMutableMapping
import pytest

def test_hookable_proxy_mutable_mapping():
    # Create a sample dictionary to be wrapped by the proxy
    sample_dict = {'key1': 'value1', 'key2': 'value2'}
    
    # Instantiate the HookableProxyMutableMapping with the sample dictionary
    hookable_map = HookableProxyMutableMapping(sample_dict)
    
    # Test if the proxy correctly wraps around the original dictionary
    assert isinstance(hookable_map, dict), "HookableProxyMutableMapping should be a subclass of dict"
    
    # Check basic operations to ensure they work as expected
    assert hookable_map['key1'] == 'value1', "Expected value for key1 is incorrect"
    with pytest.raises(KeyError):
        print(hookable_map['non_existent_key'])  # This should raise a KeyError if not handled by __key_allowed__
    
    # Test the hook functionality, assuming __key_allowed__ allows all keys for simplicity
    assert hookable_map.__key_allowed__('any_key') is True, "Expected __key_allowed__ to allow any key"

# Run this test with pytest
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
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_edge_case.py:3: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-fqhvjtlb'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-1sl1ke5g'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-urgxpgl7'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev - AttributeError: module 'collections' has no attribute 'M...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 3 warnings, 1 error in 0.15s =========================
"""