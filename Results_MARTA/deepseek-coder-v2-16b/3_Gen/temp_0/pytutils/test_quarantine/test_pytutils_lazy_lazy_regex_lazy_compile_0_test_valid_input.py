
from pytutils.lazy.lazy_regex import LazyRegex, lazy_compile
import re

def test_valid_input():
    # Create a LazyRegex object with valid regex pattern and flags
    lazy_regex = lazy_compile(r'pattern', ignorecase=True)
    
    # Check if the _real_regex attribute is not None after creation, indicating it has been compiled
    assert hasattr(lazy_regex._real_regex, 'pattern')

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
        # Create a LazyRegex object with valid regex pattern and flags
        lazy_regex = lazy_compile(r'pattern', ignorecase=True)
    
        # Check if the _real_regex attribute is not None after creation, indicating it has been compiled
>       assert hasattr(lazy_regex._real_regex, 'pattern')
E       AssertionError: assert False
E        +  where False = hasattr(None, 'pattern')
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7fbf025c6680>._real_regex

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_lazy_compile_0_test_valid_input.py:10: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-jp8spp0v'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-l4twibo7'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-jvrl9fo4'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input - AssertionError: assert False
======================== 1 failed, 3 warnings in 0.06s =========================
"""