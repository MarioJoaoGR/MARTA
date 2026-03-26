
from pytutils.lazy.lazy_import import ScopeReplacer

def test_valid_case():
    scope = {}
    
    def create_real_object(replacer, scope, name):
        return "Real Object"  # Replace with actual object creation logic
    
    replacer = ScopeReplacer(scope, create_real_object, 'real_obj')
    
    assert 'real_obj' not in scope

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
        scope = {}
    
        def create_real_object(replacer, scope, name):
            return "Real Object"  # Replace with actual object creation logic
    
        replacer = ScopeReplacer(scope, create_real_object, 'real_obj')
    
>       assert 'real_obj' not in scope
E       AssertionError: assert 'real_obj' not in {'real_obj': <pytutils.lazy.lazy_import.ScopeReplacer object at 0x7f211876b200>}

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___call___1_test_valid_case.py:12: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-vonjaxov'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-q2tdwrw7'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-5_8_ybwt'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_case - AssertionError: assert 'real_obj' not...
======================== 1 failed, 3 warnings in 0.07s =========================
"""