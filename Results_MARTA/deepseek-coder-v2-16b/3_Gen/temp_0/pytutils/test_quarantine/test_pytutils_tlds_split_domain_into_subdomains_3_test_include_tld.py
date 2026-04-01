
import pytest
from pytutils.tlds import split_domain_into_subdomains

def test_include_tld():
    # Test case for including the top-level domain (TLD) in the result
    assert split_domain_into_subdomains('this.is.a.test.skywww.net', True) == [
        'this.is.a.test.skywww.net', 'is.a.test.skywww.net', 'a.test.skywww.net',
        'test.skywww.net', 'skywww.net', 'com'
    ]

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
_______________________________ test_include_tld _______________________________

    def test_include_tld():
        # Test case for including the top-level domain (TLD) in the result
>       assert split_domain_into_subdomains('this.is.a.test.skywww.net', True) == [
            'this.is.a.test.skywww.net', 'is.a.test.skywww.net', 'a.test.skywww.net',
            'test.skywww.net', 'skywww.net', 'com'
        ]
E       AssertionError: assert ['this.is.a.t...w.net', 'net'] == ['this.is.a.t...w.net', 'com']
E         
E         At index 5 diff: 'net' != 'com'
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_3_test_include_tld.py:7: AssertionError
=============================== warnings summary ===============================
::test_include_tld
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_3_test_include_tld.py:7: DeprecationWarning: decorating class methods with @cachedmethod is deprecated
    assert split_domain_into_subdomains('this.is.a.test.skywww.net', True) == [

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-obekm2x7'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-e2euvs5c'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-smu37sm_'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_include_tld - AssertionError: assert ['this.is.a.t...
======================== 1 failed, 4 warnings in 0.17s =========================
"""