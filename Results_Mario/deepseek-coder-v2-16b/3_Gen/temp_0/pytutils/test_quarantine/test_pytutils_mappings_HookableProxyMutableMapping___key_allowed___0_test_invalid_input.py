
import pytest
from pytutils.mappings import HookableProxyMutableMapping

def test_invalid_input():
    # Create an instance of HookableProxyMutableMapping with a dictionary
    mapping = {'key1': 'value1', 'key2': 'value2'}
    proxy_map = HookableProxyMutableMapping(mapping)
    
    # Test invalid key input
    with pytest.raises(KeyError):
        proxy_map['invalid_key']  # This should raise a KeyError because '__key_allowed__' method returns False by default

    # Subclass the HookableProxyMutableMapping and override __key_allowed__ to allow only certain keys
    class CustomHookableMapping(HookableProxyMutableMapping):
        def __key_allowed__(self, key):
            return key in ['key1', 'key2']  # Allow only specific keys
    
    custom_mapping = {'key1': 'value1', 'key2': 'value2'}
    custom_hookable_mapping = CustomHookableMapping(custom_mapping)
    
    # Test valid key input after overriding __key_allowed__
    assert custom_hookable_mapping['key1'] == 'value1'  # This should pass because 'key1' is allowed
    with pytest.raises(KeyError):
        custom_hookable_mapping['invalid_key']  # This should raise a KeyError because 'invalid_key' is not allowed

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
pytutils/Test4DT_tests/test_pytutils_mappings_HookableProxyMutableMapping___key_allowed___0_test_invalid_input.py:3: in <module>
    from pytutils.mappings import HookableProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-cds5pt0m'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-z14sq6m8'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-wj0vens8'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev - AttributeError: module 'collections' has no attribute 'M...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 3 warnings, 1 error in 0.15s =========================
"""