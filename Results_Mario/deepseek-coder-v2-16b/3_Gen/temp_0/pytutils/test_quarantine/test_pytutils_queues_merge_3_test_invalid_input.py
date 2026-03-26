
import pytest
from pytutils.queues import merge, Queue
from threading import Thread

def test_invalid_input():
    with pytest.raises(TypeError):
        q1 = []  # This is an invalid input since `Queue` expects instances of `Queue`.
        out_q = merge(q1)

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
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_queues_merge_3_test_invalid_input.py:7: Failed
=============================== warnings summary ===============================
::test_invalid_input
  /usr/local/lib/python3.11/site-packages/_pytest/threadexception.py:82: PytestUnhandledThreadExceptionWarning: Exception in thread Thread-1 (push)
  
  Traceback (most recent call last):
    File "/usr/local/lib/python3.11/threading.py", line 1045, in _bootstrap_inner
      self.run()
    File "/usr/local/lib/python3.11/threading.py", line 982, in run
      self._target(*self._args, **self._kwargs)
    File "/projects/F202407648IACDCF2/mario/pytutils/pytutils/queues.py", line 27, in push
      x = in_q.get()
          ^^^^^^^^
  AttributeError: 'list' object has no attribute 'get'
  
    warnings.warn(pytest.PytestUnhandledThreadExceptionWarning(msg))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-q39oc6t_'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-gir5cqx8'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-xpgb72a8'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_input - Failed: DID NOT RAISE <class 'Type...
======================== 1 failed, 4 warnings in 0.06s =========================
"""