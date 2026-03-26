
import pytest
from functools import lru_cache
from threading import Lock
from pytutils.memo import cachedmethod, _default

def test_cachedmethod():
    @cachedmethod(cache=lru_cache(maxsize=None), key=lambda *args: args[1], lock=Lock(), typed=_default)
    def expensive_function(self, arg):
        # Some expensive computation here
        return arg + 1

    instance = None  # Assuming the method is bound to an instance
    result1 = expensive_function(instance, 1)
    assert result1 == 2

    result2 = expensive_function(instance, 1)  # Should retrieve from cache
    assert result2 == 2

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
______________________________ test_cachedmethod _______________________________

    def test_cachedmethod():
>       @cachedmethod(cache=lru_cache(maxsize=None), key=lambda *args: args[1], lock=Lock(), typed=_default)

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

method = <function test_cachedmethod.<locals>.expensive_function at 0x7f32fff73ba0>

    def decorator(method):
        # pass method to default key function for backwards compatibilty
        if key is _default:
            makekey = functools.partial(cachetools.typedkey if typed else cachetools.hashkey, method)
        else:
            makekey = key  # custom key function always receive method args
    
>       @six.wraps(method)
E       NameError: name 'six' is not defined

pytutils/pytutils/memo.py:43: NameError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-tc9jsgo5'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-8rjp3n89'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-6zxuv6bd'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_cachedmethod - NameError: name 'six' is not defined
======================== 1 failed, 3 warnings in 0.08s =========================
"""