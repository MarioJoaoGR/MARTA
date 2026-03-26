
from pytutils.lazy.simple_import import make_lazy
import sys
from types import ModuleType

def test_edge_case():
    module_path = 'math'
    make_lazy(module_path)

    # Check if the module is not imported initially
    assert module_path not in sys.modules, "Module should not be imported yet."

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
        module_path = 'math'
        make_lazy(module_path)
    
        # Check if the module is not imported initially
>       assert module_path not in sys.modules, "Module should not be imported yet."
E       AssertionError: Module should not be imported yet.
E       assert 'math' not in {'Test4DT_tests': <module 'Test4DT_tests' from '/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/__init__.py'>...ke_lazy_0_test_edge_case.py'>, '__future__': <module '__future__' from '/usr/local/lib/python3.11/__future__.py'>, ...}
E        +  where {'Test4DT_tests': <module 'Test4DT_tests' from '/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/__init__.py'>...ke_lazy_0_test_edge_case.py'>, '__future__': <module '__future__' from '/usr/local/lib/python3.11/__future__.py'>, ...} = sys.modules

pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_edge_case.py:11: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-742dr_zh'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-8jwvun1n'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-af5i1siu'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_case - AssertionError: Module should not be i...
======================== 1 failed, 3 warnings in 0.08s =========================
"""