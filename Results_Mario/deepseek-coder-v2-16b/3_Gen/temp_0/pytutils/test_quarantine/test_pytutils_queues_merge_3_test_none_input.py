
import pytest
from pytutils.queues import Queue
from threading import Thread

def merge(*in_qs, **kwargs):
    """ Merge multiple queues together.

    This function takes any number of queue objects (`in_qs`) and merges them into a single output queue (`out_q`). Additional keyword arguments can be passed to customize the behavior of the merged queue. The merging is performed concurrently using threads. Each thread pushes elements from its respective input queue to the output queue.

    Parameters:
        *in_qs (Queue): One or more queue objects that need to be merged. These should all be instances of `Queue`.
        **kwargs: Keyword arguments to customize the behavior of the merged queue. The only supported keyword argument is 'maxsize', which sets the maximum number of items allowed in the output queue. If not provided, the default maxsize will be used (if applicable).

    Returns:
        Queue: A new queue object that contains elements from all input queues.
    """
    out_q = Queue(**kwargs)
    threads = [Thread(target=out_q.put, args=(in_qs[i].get(),)) for i in range(len(in_qs))]
    for t in threads:
        t.daemon = True
        t.start()
    return out_q

def test_none_input():
    with pytest.raises(TypeError):
        merge()

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
_______________________________ test_none_input ________________________________

    def test_none_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_queues_merge_3_test_none_input.py:26: Failed
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-51yegxbu'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-0da0ai_f'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-hm7chp_d'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_none_input - Failed: DID NOT RAISE <class 'TypeErr...
======================== 1 failed, 3 warnings in 0.06s =========================
"""