
import pytest
from flutes.multiproc import StatefulPoolType
from multiprocessing import Pool, Queue
from typing import List, Any, Callable, Iterator, Mapping

class State:
    def __init__(self):
        self.queue = Queue()
    
    def process_item(self, item: int) -> int:
        # Example function to process each item in the iterable
        return item * 2

def test_error_case():
    stateful_pool = StatefulPoolType(State)
    with pytest.raises(NotImplementedError):
        results = list(stateful_pool.imap_unordered(State().process_item, range(10), chunksize=2))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
>       stateful_pool = StatefulPoolType(State)

flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_error_case.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.StatefulPoolType state=INIT pool_size=0>
processes = <class 'Test4DT_tests.test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_error_case.State'>
initializer = None, initargs = (), maxtasksperchild = None, context = None

    def __init__(self, processes=None, initializer=None, initargs=(),
                 maxtasksperchild=None, context=None):
        # Attributes initialized early to make sure that they exist in
        # __del__() if __init__() raises an exception
        self._pool = []
        self._state = INIT
    
        self._ctx = context or get_context()
        self._setup_queues()
        self._taskqueue = queue.SimpleQueue()
        # The _change_notifier queue exist to wake up self._handle_workers()
        # when the cache (self._cache) is empty or when there is a change in
        # the _state variable of the thread that runs _handle_workers.
        self._change_notifier = self._ctx.SimpleQueue()
        self._cache = _PoolCache(notifier=self._change_notifier)
        self._maxtasksperchild = maxtasksperchild
        self._initializer = initializer
        self._initargs = initargs
    
        if processes is None:
            processes = os.cpu_count() or 1
>       if processes < 1:
E       TypeError: '<' not supported between instances of 'type' and 'int'

/usr/local/lib/python3.11/multiprocessing/pool.py:204: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_StatefulPoolType_imap_unordered_0_test_error_case.py::test_error_case
============================== 1 failed in 0.11s ===============================
"""