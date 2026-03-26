
import pytest
from pytutils.mappings import ProcessLocal

def test_processlocal_initialization():
    plocal = ProcessLocal()
    assert isinstance(plocal.__mapping__, dict)

def test_processlocal_key_trans_store():
    plocal = ProcessLocal()
    key = 'test'
    result = plocal.__key_trans__(key, store=True)
    assert result == key
    assert key in plocal.__mapping__

def test_processlocal_key_trans_get():
    plocal = ProcessLocal()
    key = 'test'
    plocal.__mapping__[key] = True
    result = plocal.__key_trans__(key, get=True)
    assert result == key
    assert plocal.__mapping__[key] is True

def test_processlocal_key_trans_contains():
    plocal = ProcessLocal()
    key = 'test'
    plocal.__mapping__[key] = True
    result = plocal.__key_trans__(key, contains=True)
    assert result == key
    assert key in plocal.__mapping__

def test_processlocal_key_trans_delete():
    plocal = ProcessLocal()
    key = 'test'
    plocal.__mapping__[key] = True
    result = plocal.__key_trans__(key, delete=True)
    assert result == key
    with pytest.raises(KeyError):
        plocal.__mapping__.pop(key)

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
pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal___key_trans___0_test_valid_input.py:3: in <module>
    from pytutils.mappings import ProcessLocal
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-9xjq6327'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-a8ic71nl'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-9y9zlsr9'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev - AttributeError: module 'collections' has no attribute 'M...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 3 warnings, 1 error in 0.15s =========================
"""