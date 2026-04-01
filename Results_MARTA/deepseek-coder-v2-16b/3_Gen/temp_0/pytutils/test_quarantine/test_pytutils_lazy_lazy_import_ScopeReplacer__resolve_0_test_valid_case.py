
from pytutils.lazy.lazy_import import ScopeReplacer, IllegalUseOfScopeReplacer

def test_valid_case():
    class MyObject: pass
    
    scope = {}
    factory = lambda self, s, n: MyObject()
    replacer = ScopeReplacer(scope, factory, 'my_obj')
    
    assert 'my_obj' not in scope  # The placeholder is initially bound to the real object.
    
    obj = replacer._resolve()  # Creating the real object for the first time.
    assert isinstance(obj, MyObject) and 'my_obj' in scope  # Now the real object is in the scope.

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
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        class MyObject: pass
    
        scope = {}
        factory = lambda self, s, n: MyObject()
        replacer = ScopeReplacer(scope, factory, 'my_obj')
    
>       assert 'my_obj' not in scope  # The placeholder is initially bound to the real object.
E       AssertionError: assert 'my_obj' not in {'my_obj': <pytutils.lazy.lazy_import.ScopeReplacer object at 0x7f5c9e0de180>}

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0_test_valid_case.py:11: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-a08tg98b'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-i4we25_0'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-19zkgiy9'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_case - AssertionError: assert 'my_obj' not i...
======================== 1 failed, 3 warnings in 0.08s =========================
"""