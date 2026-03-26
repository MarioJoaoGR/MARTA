
import pytest
from pytutils.log import _ensure_configured, configure

# Define a fixture to provide a mock for _CONFIGURED
@pytest.fixture(autouse=True)
def setup_mock_config():
    # Create a mutable default value for _CONFIGURED
    global _CONFIGURED
    _CONFIGURED = []

def test_already_configured():
    # Initially, _CONFIGURED should be empty
    assert not _CONFIGURED
    
    # Call the function with no parameters to ensure configuration
    _ensure_configured()
    
    # After calling the function, _CONFIGURED should have a True value
    assert len(_CONFIGURED) == 1 and _CONFIGURED[0] is True

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
___________________________ test_already_configured ____________________________

    def test_already_configured():
        # Initially, _CONFIGURED should be empty
        assert not _CONFIGURED
    
        # Call the function with no parameters to ensure configuration
        _ensure_configured()
    
        # After calling the function, _CONFIGURED should have a True value
>       assert len(_CONFIGURED) == 1 and _CONFIGURED[0] is True
E       assert (0 == 1)
E        +  where 0 = len([])

pytutils/Test4DT_tests/test_pytutils_log__ensure_configured_0_test_already_configured.py:20: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-etntr94f'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-_zu1qiky'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-iquq5vut'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_already_configured - assert (0 == 1)
======================== 1 failed, 3 warnings in 0.06s =========================
"""