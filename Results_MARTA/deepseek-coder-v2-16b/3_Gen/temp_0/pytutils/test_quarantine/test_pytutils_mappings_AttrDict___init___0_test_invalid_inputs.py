
import pytest
from pytutils.mappings import AttrDict

def test_invalid_inputs():
    # Test that AttrDict does not accept non-dictionary types as input
    with pytest.raises(TypeError):
        AttrDict([1, 2, 3])  # List instead of dictionary
    
    with pytest.raises(TypeError):
        AttrDict((1, 2, 3))  # Tuple instead of dictionary
    
    with pytest.raises(TypeError):
        AttrDict({1: 'a', 2: 'b'})  # Dictionary with non-string keys
    
    with pytest.raises(TypeError):
        AttrDict('not a dict')  # String instead of dictionary
    
    with pytest.raises(TypeError):
        AttrDict(123)  # Integer instead of dictionary
    
    with pytest.raises(TypeError):
        AttrDict(None)  # None type instead of dictionary

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
pytutils/Test4DT_tests/test_pytutils_mappings_AttrDict___init___0_test_invalid_inputs.py:3: in <module>
    from pytutils.mappings import AttrDict
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-7zzbdvs6'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-1z8ub5up'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-xulwn7xc'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev - AttributeError: module 'collections' has no attribute 'M...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 3 warnings, 1 error in 0.16s =========================
"""