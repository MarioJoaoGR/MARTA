
import pytest
from pytutils.mappings import ProxyMutableMapping

def test_valid_input():
    a = dict(whoa=True, hello=[1,2,3], why='always')
    b = ProxyMutableMapping(a)
    
    # Check initial representation
    assert repr(b) == "<ProxyMutableMapping {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>"
    
    # Set a new key-value pair
    b['nice'] = False
    assert b['nice'] == False
    
    # Check the representation after setting a new value
    assert repr(b) == "<ProxyMutableMapping {'whoa': True, 'hello': [1, 2, 3], 'why': 'always', 'nice': False}>"
    
    # Verify that the change is reflected in the original dictionary
    assert b._ProxyMutableMapping__mapping == {'whoa': True, 'hello': [1, 2, 3], 'why': 'always', 'nice': False}

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
pytutils/Test4DT_tests/test_pytutils_mappings_ProxyMutableMapping__set_mapping_0_test_valid_input.py:3: in <module>
    from pytutils.mappings import ProxyMutableMapping
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-3kfwiusq'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-sc38gzsb'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-2xpo_2bp'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev - AttributeError: module 'collections' has no attribute 'M...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 3 warnings, 1 error in 0.12s =========================
"""