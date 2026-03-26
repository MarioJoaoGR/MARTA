
import pytest
from functools import lru_cache
from threading import Lock
import warnings
import six
import cachetools
from pytutils.memo import cachedmethod, _default, CachedException

# Test cases for the cachedmethod decorator

def test_cachedmethod_basic():
    @cachedmethod(cache=lru_cache(maxsize=None), key=lambda *args: args[1], lock=Lock(), typed=False)
    def expensive_function(self, arg):
        return "result"
    
    # Assuming the function is used in a context where self and arg are defined
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0.py F            [100%]

=================================== FAILURES ===================================
___________________________ test_cachedmethod_basic ____________________________

    def test_cachedmethod_basic():
>       @cachedmethod(cache=lru_cache(maxsize=None), key=lambda *args: args[1], lock=Lock(), typed=False)

pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cache = <function lru_cache.<locals>.decorating_function at 0x7f22518959e0>
key = <function test_cachedmethod_basic.<locals>.<lambda> at 0x7f22518171a0>
lock = <unlocked _thread.lock object at 0x7f225181b400>, typed = False
cached_exception = None

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
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0.py::test_cachedmethod_basic
============================== 1 failed in 0.06s ===============================
"""