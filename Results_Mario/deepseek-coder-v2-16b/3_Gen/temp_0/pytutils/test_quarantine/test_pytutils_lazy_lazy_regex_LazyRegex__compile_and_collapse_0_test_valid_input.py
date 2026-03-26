
import pytest
import re
from pytutils.lazy.lazy_regex import LazyRegex

@pytest.mark.parametrize("pattern, kwargs", [
    (r'\d+', {'ignorecase': True}),
    (r'[a-z]+', {}),
    (r'hello', {'ignorecase': False})
])
def test_valid_input(pattern, kwargs):
    lazy_regex = LazyRegex(pattern, **kwargs)
    assert isinstance(lazy_regex._real_regex, re.Pattern)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

../../../dev FFF                                                         [100%]

=================================== FAILURES ===================================
________________________ test_valid_input[\\d+-kwargs0] ________________________

pattern = '\\d+', kwargs = {'ignorecase': True}

    @pytest.mark.parametrize("pattern, kwargs", [
        (r'\d+', {'ignorecase': True}),
        (r'[a-z]+', {}),
        (r'hello', {'ignorecase': False})
    ])
    def test_valid_input(pattern, kwargs):
>       lazy_regex = LazyRegex(pattern, **kwargs)
E       TypeError: LazyRegex.__init__() got an unexpected keyword argument 'ignorecase'

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py:12: TypeError
_______________________ test_valid_input[[a-z]+-kwargs1] _______________________

pattern = '[a-z]+', kwargs = {}

    @pytest.mark.parametrize("pattern, kwargs", [
        (r'\d+', {'ignorecase': True}),
        (r'[a-z]+', {}),
        (r'hello', {'ignorecase': False})
    ])
    def test_valid_input(pattern, kwargs):
        lazy_regex = LazyRegex(pattern, **kwargs)
>       assert isinstance(lazy_regex._real_regex, re.Pattern)
E       AssertionError: assert False
E        +  where False = isinstance(None, <class 're.Pattern'>)
E        +    where None = <pytutils.lazy.lazy_regex.LazyRegex object at 0x7ff8e9383c70>._real_regex
E        +    and   <class 're.Pattern'> = re.Pattern

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py:13: AssertionError
_______________________ test_valid_input[hello-kwargs2] ________________________

pattern = 'hello', kwargs = {'ignorecase': False}

    @pytest.mark.parametrize("pattern, kwargs", [
        (r'\d+', {'ignorecase': True}),
        (r'[a-z]+', {}),
        (r'hello', {'ignorecase': False})
    ])
    def test_valid_input(pattern, kwargs):
>       lazy_regex = LazyRegex(pattern, **kwargs)
E       TypeError: LazyRegex.__init__() got an unexpected keyword argument 'ignorecase'

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex__compile_and_collapse_0_test_valid_input.py:12: TypeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-z15y1rbr'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-ci9wz99d'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-gelnr1mn'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input[\\d+-kwargs0] - TypeError: LazyRegex._...
FAILED ../../../dev/::test_valid_input[[a-z]+-kwargs1] - AssertionError: asse...
FAILED ../../../dev/::test_valid_input[hello-kwargs2] - TypeError: LazyRegex....
======================== 3 failed, 3 warnings in 0.08s =========================
"""