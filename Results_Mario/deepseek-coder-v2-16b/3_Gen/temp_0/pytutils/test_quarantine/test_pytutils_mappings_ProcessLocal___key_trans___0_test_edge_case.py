
import pytest
from pytutils.mappings import ProcessLocal

@pytest.fixture
def process_local():
    return ProcessLocal()

def test_key_trans_basic(process_local):
    # Test basic functionality of __key_trans__ method
    assert process_local.__key_trans__('test') == 'test'

def test_key_trans_store(process_local):
    # Test storing a key
    process_local.__key_trans__('test', store=True)
    assert process_local['test'] == True

def test_key_trans_get(process_local):
    # Test getting an existing key
    process_local['test'] = True
    assert process_local.__key_trans__('test', get=True) == True

def test_key_trans_contains(process_local):
    # Test checking existence of a key
    process_local['test'] = True
    assert process_local.__key_trans__('test', contains=True) == 'test'

def test_key_trans_delete(process_local):
    # Test deleting a key
    process_local['test'] = True
    process_local.__key_trans__('test', delete=True)
    with pytest.raises(KeyError):
        process_local['test']

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
pytutils/Test4DT_tests/test_pytutils_mappings_ProcessLocal___key_trans___0_test_edge_case.py:3: in <module>
    from pytutils.mappings import ProcessLocal
pytutils/pytutils/mappings.py:23: in <module>
    class ProxyMutableMapping(collections.MutableMapping):
E   AttributeError: module 'collections' has no attribute 'MutableMapping'
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-d9l9vc69'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-m7qeykt2'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-q8i6e6ea'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev - AttributeError: module 'collections' has no attribute 'M...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 3 warnings, 1 error in 0.16s =========================
"""