
import pytest
from flutes.multiproc import PoolWrapper
import multiprocessing as mp
import functools
from typing import Callable, Iterator, Iterable, Any, Dict
from queue import Empty
import time

def _gather_fn(queue: mp.Queue, fn: Callable[[Any], Iterator[Any]], item: Any) -> None:
    result = fn(item)
    for r in result:
        queue.put(r)
    queue.put(END_SIGNATURE)

END_SIGNATURE = object()

class CustomMPReducer:
    def __init__(self):
        self.queue = mp.Queue()

    def Manager(self):
        return self

@pytest.fixture
def pool():
    return PoolWrapper()

# Test cases for imap method
def test_imap(pool):
    results = list(pool.imap([1, 2, 3], lambda x: x * x))
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0.py F     [100%]

=================================== FAILURES ===================================
__________________________________ test_imap ___________________________________

pool = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_imap(pool):
>       results = list(pool.imap([1, 2, 3], lambda x: x * x))

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <multiprocessing.pool.IMapIterator object at 0x7f5a3e67f190>
timeout = None

    def next(self, timeout=None):
        with self._cond:
            try:
                item = self._items.popleft()
            except IndexError:
                if self._index == self._length:
                    self._pool = None
                    raise StopIteration from None
                self._cond.wait(timeout)
                try:
                    item = self._items.popleft()
                except IndexError:
                    if self._index == self._length:
                        self._pool = None
                        raise StopIteration from None
                    raise TimeoutError from None
    
        success, value = item
        if success:
            return value
>       raise value
E       TypeError: 'function' object is not iterable

/usr/local/lib/python3.11/multiprocessing/pool.py:873: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0.py::test_imap
============================== 1 failed in 0.20s ===============================
"""