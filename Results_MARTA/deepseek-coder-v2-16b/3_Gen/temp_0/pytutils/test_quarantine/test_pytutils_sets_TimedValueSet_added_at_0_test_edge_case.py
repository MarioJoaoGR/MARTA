
import pytest
from pytutils.sets import TimedValueSet
import time

@pytest.fixture
def timed_value_set():
    return TimedValueSet(_store=set(), _meta={}, _initial=None, _meta_func=lambda value, **kwargs: time.time())

def test_added_at(timed_value_set):
    # Ensure that the added_at method returns a value close to the current time when it was created
    assert isinstance(timed_value_set.added_at(), float)

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

../../../dev E                                                           [100%]

==================================== ERRORS ====================================
_______________________ ERROR at setup of test_added_at ________________________

    @pytest.fixture
    def timed_value_set():
>       return TimedValueSet(_store=set(), _meta={}, _initial=None, _meta_func=lambda value, **kwargs: time.time())
E       TypeError: TimedValueSet.__init__() got an unexpected keyword argument '_store'

pytutils/Test4DT_tests/test_pytutils_sets_TimedValueSet_added_at_0_test_edge_case.py:8: TypeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-wp6neogu'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-8qq802t6'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-42k_1fk8'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR ../../../dev/::test_added_at - TypeError: TimedValueSet.__init__() got ...
========================= 3 warnings, 1 error in 0.09s =========================
"""