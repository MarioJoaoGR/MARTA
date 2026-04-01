
from pytutils.lazy.lazy_import import ScopeReplacer

def test_edge_case():
    scope = {}
    
    def my_factory(replacer, scope, name):
        return "Real Object"
    
    replacer = ScopeReplacer(scope, my_factory, 'real_obj')
    
    # At this point, `replacer` is a placeholder in the scope.
    # To get the real object:
    real_object = replacer()  # This will call __call__ and create the real object.
    
    assert real_object == "Real Object"

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
________________________________ test_edge_case ________________________________

    def test_edge_case():
        scope = {}
    
        def my_factory(replacer, scope, name):
            return "Real Object"
    
        replacer = ScopeReplacer(scope, my_factory, 'real_obj')
    
        # At this point, `replacer` is a placeholder in the scope.
        # To get the real object:
>       real_object = replacer()  # This will call __call__ and create the real object.

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___call___1_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ScopeReplacer object at 0x7fe89d85e140>
args = (), kwargs = {}, obj = 'Real Object'

    def __call__(self, *args, **kwargs):
        obj = object.__getattribute__(self, '_resolve')()
>       return obj(*args, **kwargs)
E       TypeError: 'str' object is not callable

pytutils/pytutils/lazy/lazy_import.py:191: TypeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-827_ld9n'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-6n6x10hj'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-vk62a3uc'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_case - TypeError: 'str' object is not callable
======================== 1 failed, 3 warnings in 0.09s =========================
"""