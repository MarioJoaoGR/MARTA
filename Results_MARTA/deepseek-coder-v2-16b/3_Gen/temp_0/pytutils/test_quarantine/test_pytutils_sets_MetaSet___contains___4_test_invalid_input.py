
import pytest
from pytutils.sets import MetaSet

def test_invalid_input():
    meta_set = MetaSet()
    
    with pytest.raises(TypeError):
        assert 'a' in meta_set  # This will raise a TypeError because 'a' is a string and not an integer

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

../../../dev F                                                           [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        meta_set = MetaSet()
    
        with pytest.raises(TypeError):
>           assert 'a' in meta_set  # This will raise a TypeError because 'a' is a string and not an integer
E           AssertionError: assert 'a' in MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7ff5a2e0e8e0>, _store=set(), _meta={}, _initial=None)

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___contains___4_test_invalid_input.py:9: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-7h_8v6b5'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-4j7q882b'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-61jg8fdy'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_input - AssertionError: assert 'a' in Meta...
======================== 1 failed, 3 warnings in 0.08s =========================
"""