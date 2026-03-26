
import pytest
from flutes.multiproc import ProgressBarManager
import functools
import multiprocessing as mp
import time
import random
from typing import List, Iterable, Dict, Any, Optional, Union, Literal, Iterator, overload

# Mock functions for testing
def run(xs: List[int], *, bar) -> int:
    result = 0
    for idx, x in enumerate(xs):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(1, postfix={"sum": result})
        if (idx + 1) % 100 == 0:
            flutes.log(f"Processed {idx + 1} samples")
    return result

def run2(xs: List[int], *, bar) -> int:
    result = 0
    for idx, x in enumerate(bar.iter(xs)):
        result += x
        time.sleep(random.uniform(0.01, 0.2))
        bar.update(postfix={"sum": result})
        if (idx + 1) % 100 == 0:
            flutes.log(f"Processed {idx + 1} samples")
    return result

# Mock flutes module for testing
class flutes:
    @staticmethod
    def get_worker_id():
        return random.randint(1, 10)
    
    @staticmethod
    def log(*args):
        print(*args)
    
    class safe_pool:
        def __init__(self, size):
            self.size = size
        
        def __enter__(self):
            return self
        
        def imap_unordered(self, func, iterable):
            with mp.Pool(self.size) as pool:
                results = pool.imap_unordered(func, iterable)
                for result in results:
                    yield result
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

# Test cases for ProgressBarManager class
def test_ProgressBarManager_default():
    manager = ProgressBarManager(verbose=True)
    run_fn = functools.partial(run, bar=manager.proxy)
    data = list(range(1000))  # Large enough to see multiple updates
    
    with flutes.safe_pool(4) as pool:
        for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):
            flutes.log(f"Processed {idx + 1} arrays")
    
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

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___0.py F [100%]

=================================== FAILURES ===================================
_______________________ test_ProgressBarManager_default ________________________
multiprocessing.pool.RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 125, in worker
    result = (True, func(*args, **kwds))
                    ^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___0.py", line 13, in run
    for idx, x in enumerate(xs):
                  ^^^^^^^^^^^^^
TypeError: 'int' object is not iterable
"""

The above exception was the direct cause of the following exception:

    def test_ProgressBarManager_default():
        manager = ProgressBarManager(verbose=True)
        run_fn = functools.partial(run, bar=manager.proxy)
        data = list(range(1000))  # Large enough to see multiple updates
    
        with flutes.safe_pool(4) as pool:
>           for idx, _ in enumerate(pool.imap_unordered(run_fn, data)):

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___0.py:64: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___0.py:51: in imap_unordered
    for result in results:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <multiprocessing.pool.IMapUnorderedIterator object at 0x7f4da7668e50>
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
E       TypeError: 'int' object is not iterable

/usr/local/lib/python3.11/multiprocessing/pool.py:873: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___0.py::test_ProgressBarManager_default
============================== 1 failed in 0.14s ===============================
"""