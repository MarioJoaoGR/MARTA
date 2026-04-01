
import pytest
from pytutils.meth import bind

def test_bind_edge_cases():
    # Test when instance is None
    with pytest.raises(TypeError):
        bind(None, lambda self: None, 'method')

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
_____________________________ test_bind_edge_cases _____________________________

    def test_bind_edge_cases():
        # Test when instance is None
        with pytest.raises(TypeError):
>           bind(None, lambda self: None, 'method')

pytutils/Test4DT_tests/test_pytutils_meth_bind_1_test_edge_cases.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

instance = None
func = <function test_bind_edge_cases.<locals>.<lambda> at 0x7fa7fd75a160>
as_name = 'method'

    def bind(instance, func, as_name):
        """
        Turn a function to a bound method on an instance
    
        >>> class Foo(object):
        ...     def __init__(self, x, y):
        ...         self.x = x
        ...         self.y = y
        >>> foo = Foo(2, 3)
        >>> my_unbound_method = lambda self: self.x * self.y
        >>> bind(foo, my_unbound_method, 'multiply')
        >>> foo.multiply()  # noinspection PyUnresolvedReferences
        6
    
        :param object instance: some object
        :param callable func: unbound method (i.e. a function that takes `self` argument, that you now
            want to be bound to this class as a method)
        :param str as_name: name of the method to create on the object
        """
>       setattr(instance, as_name, func.__get__(instance, instance.__class__))
E       AttributeError: 'NoneType' object has no attribute 'method'

pytutils/pytutils/meth.py:20: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-kenbugbq'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-7ylzydua'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-9cgflqkt'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_bind_edge_cases - AttributeError: 'NoneType' objec...
======================== 1 failed, 3 warnings in 0.08s =========================
"""