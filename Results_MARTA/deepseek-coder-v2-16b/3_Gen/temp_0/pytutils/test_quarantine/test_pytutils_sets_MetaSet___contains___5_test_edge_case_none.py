
import pytest
from pytutils.sets import MetaSet

def test_edge_case_none():
    meta_set = MetaSet()
    
    # Adding None should not raise an error and should not affect the set
    with pytest.raises(KeyError):  # Expecting a KeyError because None is not in the set
        assert None in meta_set

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
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        meta_set = MetaSet()
    
        # Adding None should not raise an error and should not affect the set
        with pytest.raises(KeyError):  # Expecting a KeyError because None is not in the set
>           assert None in meta_set
E           assert None in MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7f47302ef880>, _store=set(), _meta={}, _initial=None)

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___contains___5_test_edge_case_none.py:10: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-cuoj47is'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-1wehpg50'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-djohsmhx'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_case_none - assert None in MetaSet(_meta_func...
======================== 1 failed, 3 warnings in 0.09s =========================
"""