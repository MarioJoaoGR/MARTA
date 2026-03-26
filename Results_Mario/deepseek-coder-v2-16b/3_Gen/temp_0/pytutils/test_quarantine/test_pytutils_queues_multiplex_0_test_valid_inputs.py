
import pytest
from queue import Queue
from threading import Thread
from pytutils.queues import multiplex

def test_valid_inputs():
    in_q = Queue()
    q1, q2, q3 = multiplex(in_q, count=3)

    # Add items to the input queue
    in_q.put("item1")
    in_q.put("item2")

    # Check if items are present in all output queues
    assert not q1.empty()
    assert not q2.empty()
    assert not q3.empty()

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
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        in_q = Queue()
        q1, q2, q3 = multiplex(in_q, count=3)
    
        # Add items to the input queue
        in_q.put("item1")
        in_q.put("item2")
    
        # Check if items are present in all output queues
>       assert not q1.empty()
E       assert not True
E        +  where True = empty()
E        +    where empty = <queue.Queue object at 0x7f92c2b4dd50>.empty

pytutils/Test4DT_tests/test_pytutils_queues_multiplex_0_test_valid_inputs.py:16: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-klralcm3'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-sbap2php'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-h8ixuahw'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_inputs - assert not True
======================== 1 failed, 3 warnings in 0.07s =========================
"""