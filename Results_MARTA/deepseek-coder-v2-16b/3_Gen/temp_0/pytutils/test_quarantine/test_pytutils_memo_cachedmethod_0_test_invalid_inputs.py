
import pytest
from pytutils.memo import cachedmethod
from functools import lru_cache
from threading import Lock
import warnings
import six
import cachetools

# Mock the necessary modules and classes for testing
class CachedException(Exception):
    pass

def test_invalid_inputs():
    with pytest.warns(DeprecationWarning):
        @cachedmethod(cache=lru_cache(maxsize=None), key="arg1", lock=Lock(), typed=False)
        def method(self, arg):
            return arg

    # Test that the deprecation warning is raised when 'typed' is used
    with pytest.warns(DeprecationWarning):
        @cachedmethod(cache=lru_cache(maxsize=None), key="arg1", lock=Lock(), typed=True)
        def method2(self, arg):
            return arg

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
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.warns(DeprecationWarning):
>           @cachedmethod(cache=lru_cache(maxsize=None), key="arg1", lock=Lock(), typed=False)

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_invalid_inputs.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cache = <function lru_cache.<locals>.decorating_function at 0x7fbd71102a20>
key = [], lock = <unlocked _thread.lock object at 0x7fbd70b99180>
typed = 'arg1', cached_exception = None

    def cachedmethod(cache, key=_default, lock=None, typed=_default, cached_exception=None):
        """Decorator to wrap a class or instance method with a memoizing
        callable that saves results in a cache.
    
        You can also specify a cached exception to cache and re-throw as well.
    
        Originally from cachetools, but modified to support caching certain exceptions.
        """
        if key is not _default and not callable(key):
            key, typed = _default, key
        if typed is not _default:
>           warnings.warn(
                "Passing 'typed' to cachedmethod() is deprecated, "
                "use 'key=typedkey' instead", DeprecationWarning, 2
            )
E           NameError: name 'warnings' is not defined

pytutils/pytutils/memo.py:31: NameError

During handling of the above exception, another exception occurred:

    def test_invalid_inputs():
>       with pytest.warns(DeprecationWarning):
E       Failed: DID NOT WARN. No warnings of type (<class 'DeprecationWarning'>,) were emitted.
E        Emitted warnings: [].

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_invalid_inputs.py:15: Failed
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-_3k66l4b'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-vawx3ygq'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-b6zprdge'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_inputs - Failed: DID NOT WARN. No warnings...
======================== 1 failed, 3 warnings in 0.10s =========================
"""