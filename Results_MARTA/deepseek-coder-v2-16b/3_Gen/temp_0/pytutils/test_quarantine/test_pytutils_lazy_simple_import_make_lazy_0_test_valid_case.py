
from unittest.mock import patch
import pytest
import sys
from pytutils.lazy.simple_import import make_lazy

@pytest.mark.parametrize("module_path", ["math"])
def test_valid_case(module_path):
    with patch('sys.modules', {'math': None}):  # Mock the sys.modules to start without math
        make_lazy(module_path)
        assert module_path not in sys.modules, f"Module {module_path} should not be imported yet."

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
____________________________ test_valid_case[math] _____________________________

module_path = 'math'

    @pytest.mark.parametrize("module_path", ["math"])
    def test_valid_case(module_path):
        with patch('sys.modules', {'math': None}):  # Mock the sys.modules to start without math
            make_lazy(module_path)
>           assert module_path not in sys.modules, f"Module {module_path} should not be imported yet."
E           AssertionError: Module math should not be imported yet.
E           assert 'math' not in {'math': <pytutils.lazy.simple_import.make_lazy.<locals>.LazyModule object at 0x7f5441699c50>}
E            +  where {'math': <pytutils.lazy.simple_import.make_lazy.<locals>.LazyModule object at 0x7f5441699c50>} = sys.modules

pytutils/Test4DT_tests/test_pytutils_lazy_simple_import_make_lazy_0_test_valid_case.py:11: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-jtiu5m0z'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-qk0qmp8f'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-orhee9iy'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_case[math] - AssertionError: Module math sho...
======================== 1 failed, 3 warnings in 0.08s =========================
"""