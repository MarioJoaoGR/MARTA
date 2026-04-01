
import pytest
from pytutils.lazy.lazy_regex import LazyRegex, InvalidPattern
import re

def test_edge_case():
    lazy_regex = LazyRegex(r'\d+')
    assert lazy_regex._real_regex is None
    
    # When accessing a method that triggers the compilation
    matches = lazy_regex.findall("123abc")
    assert isinstance(lazy_regex._real_regex, re.Pattern)
    assert matches == ['123']

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
        lazy_regex = LazyRegex(r'\d+')
        assert lazy_regex._real_regex is None
    
        # When accessing a method that triggers the compilation
>       matches = lazy_regex.findall("123abc")

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__real_re_compile_0_test_edge_case.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/lazy/lazy_regex.py:159: in __getattr__
    self._compile_and_collapse()
pytutils/pytutils/lazy/lazy_regex.py:126: in _compile_and_collapse
    self._real_regex = self._real_re_compile(*self._regex_args,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7f595da2e830>
args = ('\\', 'd', '+'), kwargs = {}

    def _real_re_compile(self, *args, **kwargs):
        """Thunk over to the original re.compile"""
        try:
>           return _real_re_compile(*args, **kwargs)
E           TypeError: compile() takes from 1 to 2 positional arguments but 3 were given

pytutils/pytutils/lazy/lazy_regex.py:134: TypeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-ohcgz6lg'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-pg3l02vt'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-ywovayud'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_case - TypeError: compile() takes from 1 to 2...
======================== 1 failed, 3 warnings in 0.08s =========================
"""