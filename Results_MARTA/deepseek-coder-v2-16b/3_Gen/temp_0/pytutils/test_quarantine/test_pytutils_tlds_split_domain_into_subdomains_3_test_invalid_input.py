
import pytest
from pytutils.tlds import split_domain_into_subdomains

def test_invalid_input():
    domain = 'invalid-domain'
    with pytest.raises(ValueError):
        split_domain_into_subdomains(domain)

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
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        domain = 'invalid-domain'
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_3_test_invalid_input.py:7: Failed
=============================== warnings summary ===============================
::test_invalid_input
  /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_tlds_split_domain_into_subdomains_3_test_invalid_input.py:8: DeprecationWarning: decorating class methods with @cachedmethod is deprecated
    split_domain_into_subdomains(domain)

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-h39hgpye'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-2n4aso3q'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-wf58v_6c'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_input - Failed: DID NOT RAISE <class 'Valu...
======================== 1 failed, 4 warnings in 0.17s =========================
"""