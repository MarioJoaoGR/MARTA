
import pytest
from unittest.mock import MagicMock
from pytutils.lazy.lazy_import import ScopeReplacer

def test_valid_input():
    scope = {}
    
    def factory(self, scope, name):
        return RealObject(name)
    
    class RealObject:
        def __init__(self, value):
            self.value = value
    
    replacer = ScopeReplacer(scope, factory, 'real_obj')
    
    assert isinstance(replacer._resolve(), RealObject)
    assert scope['real_obj'].value == 'real_obj'

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
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        scope = {}
    
        def factory(self, scope, name):
            return RealObject(name)
    
        class RealObject:
            def __init__(self, value):
                self.value = value
    
        replacer = ScopeReplacer(scope, factory, 'real_obj')
    
>       assert isinstance(replacer._resolve(), RealObject)

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___setattr___1_test_valid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ScopeReplacer object at 0x7f0e730ac880>
attr = '_resolve'

    def __getattribute__(self, attr):
        obj = object.__getattribute__(self, '_resolve')()
>       return getattr(obj, attr)
E       AttributeError: 'RealObject' object has no attribute '_resolve'

pytutils/pytutils/lazy/lazy_import.py:183: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-ak_c82n6'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-e0oog_7_'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-efltz_us'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input - AttributeError: 'RealObject' object ...
======================== 1 failed, 3 warnings in 0.08s =========================
"""