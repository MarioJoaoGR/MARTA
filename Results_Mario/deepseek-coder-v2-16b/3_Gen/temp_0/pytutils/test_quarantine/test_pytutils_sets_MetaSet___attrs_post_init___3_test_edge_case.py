
import pytest
from pytutils.sets import MetaSet
from datetime import datetime

@pytest.fixture
def meta_set():
    return MetaSet()

def test_update(meta_set):
    lst = [1, 2, 3, 4]
    meta_set._initial = lst
    meta_set.__attrs_post_init__()

    assert len(meta_set._store) == 4
    for item in lst:
        assert item in meta_set._store
    assert all(item in meta_set._meta and 'added_at' in meta_set._meta[item] for item in lst)

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
_________________________________ test_update __________________________________

meta_set = <[AttributeError("'MetaSet' object has no attribute '_initial'") raised in repr()] MetaSet object at 0x7f0a478b3c10>

    def test_update(meta_set):
        lst = [1, 2, 3, 4]
        meta_set._initial = lst
        meta_set.__attrs_post_init__()
    
        assert len(meta_set._store) == 4
        for item in lst:
            assert item in meta_set._store
>       assert all(item in meta_set._meta and 'added_at' in meta_set._meta[item] for item in lst)

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___attrs_post_init___3_test_edge_case.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7f0a46c867a0>

>   assert all(item in meta_set._meta and 'added_at' in meta_set._meta[item] for item in lst)
E   TypeError: argument of type 'int' is not iterable

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet___attrs_post_init___3_test_edge_case.py:18: TypeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-0m144oq_'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-blnxsqk9'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-4313rify'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_update - TypeError: argument of type 'int' is not ...
======================== 1 failed, 3 warnings in 0.09s =========================
"""