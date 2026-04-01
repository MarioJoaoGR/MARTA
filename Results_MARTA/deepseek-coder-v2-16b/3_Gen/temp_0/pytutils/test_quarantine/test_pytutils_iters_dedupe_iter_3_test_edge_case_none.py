
import pytest
from pytutils.iters import dedupe_iter

def test_edge_case_none():
    # Test that None is ignored in the iterator
    result = list(dedupe_iter([1, 2, None, 2, 3, None]))
    assert result == [1, 2, 3]

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
        # Test that None is ignored in the iterator
        result = list(dedupe_iter([1, 2, None, 2, 3, None]))
>       assert result == [1, 2, 3]
E       assert [1, 2, None, 3] == [1, 2, 3]
E         
E         At index 2 diff: None != 3
E         Left contains one more item: 3
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_iters_dedupe_iter_3_test_edge_case_none.py:8: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-f4jthp70'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-blnd2ow4'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-psejwabk'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_case_none - assert [1, 2, None, 3] == [1, 2, 3]
======================== 1 failed, 3 warnings in 0.06s =========================
"""