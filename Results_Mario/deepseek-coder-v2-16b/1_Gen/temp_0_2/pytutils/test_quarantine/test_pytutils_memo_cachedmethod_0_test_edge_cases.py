
from pytutils.memo import cachedmethod
import warnings
import functools
import cachetools
import six

def cachedmethod(cache, key=_default, lock=None, typed=_default, cached_exception=None):
    """Decorator to wrap a class or instance method with a memoizing callable that saves results in a cache.

    You can also specify a cached exception to cache and re-throw as well.

    Parameters:
        cache (callable): A function that returns the cache for the given instance.
        key (callable or str, optional): Function to compute a key from the method arguments. If not provided, it defaults to using `cachetools.typedkey` if `typed` is True, otherwise `cachetools.hashkey`.
        lock (callable, optional): A function that returns a context manager for locking access to the cache.
        typed (bool, optional): Whether to use type information in the key computation. This parameter is deprecated and will be removed; instead, use `key=typedkey` for similar functionality.
        cached_exception (type, optional): The exception type to cache and re-throw as a `CachedException`.

    Returns:
        callable: The decorated method.

    Example:
        ```python
        from pytutils.memo import cachedmethod
        from threading import Lock

        class MyClass:
            def __init__(self):
                self._cache = {}

            @cachedmethod(lambda inst: inst._cache, key=lambda inst, *args: args[0])
            def expensive_function(self, arg1):
                # Perform some expensive computation here
                return arg1 * 2

        my_instance = MyClass()
        print(my_instance.expensive_function(5))  # First call will be slow, subsequent calls will be fast due to caching
        ```
    """
    if key is not _default and not callable(key):
        key, typed = _default, key
    if typed is not _default:
        warnings.warn(
            "Passing 'typed' to cachedmethod() is deprecated, "
            "use 'key=typedkey' instead", DeprecationWarning, 2
        )

    def decorator(method):
        # pass method to default key function for backwards compatibility
        if key is _default:
            makekey = functools.partial(cachetools.typedkey if typed else cachetools.hashkey, method)
        else:
            makekey = key  # custom key function always receive method args

        @six.wraps(method)
        def wrapper(self, *args, **kwargs):
            c = cache(self)
            ret = _sentinel

            if c is not None:
                k = makekey(self, *args, **kwargs)
                try:
                    if lock is not None:
                        with lock(self):
                            ret = c[k]
                    else:
                        ret = c[k]
                except KeyError:
                    pass  # key not found

            if ret is _sentinel:
                try:
                    ret = method(self, *args, **kwargs)
                except cached_exception as e:
                    ret = CachedException(e)

                if c is not None:
                    try:
                        if lock is not None:
                            with lock(self):
                                c[k] = ret
                        else:
                            c[k] = ret
                    except ValueError:
                        pass  # value too large

            if isinstance(ret, CachedException):
                ret()
            else:
                return ret

        # deprecated wrapper attribute
        def getter(self):
            warnings.warn('%s.cache is deprecated' % method.__name__, DeprecationWarning, 2)
            return cache(self)

        wrapper.cache = getter
        return wrapper

    return decorator

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_memo_cachedmethod_0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:8:0: E0102: function already defined line 2 (function-redefined)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:8:28: E0602: Undefined variable '_default' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:8:55: E0602: Undefined variable '_default' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:41:18: E0602: Undefined variable '_default' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:42:21: E0602: Undefined variable '_default' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:43:20: E0602: Undefined variable '_default' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:51:18: E0602: Undefined variable '_default' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:52:40: E1101: Module 'cachetools' has no 'typedkey' member (no-member)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:52:74: E1101: Module 'cachetools' has no 'hashkey' member (no-member)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:59:18: E0602: Undefined variable '_sentinel' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:72:22: E0602: Undefined variable '_sentinel' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:76:26: E0602: Undefined variable 'CachedException' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_memo_cachedmethod_0_test_edge_cases.py:88:31: E0602: Undefined variable 'CachedException' (undefined-variable)


"""