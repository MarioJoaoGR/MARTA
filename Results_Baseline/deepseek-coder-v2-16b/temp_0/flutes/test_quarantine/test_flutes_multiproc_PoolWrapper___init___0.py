
# Module: flutes.multiproc
import pytest
from multiprocessing import Pool
from flutes.multiproc import PoolWrapper

# Test cases for imap method
def test_imap():
    pool = PoolWrapper()
    results = pool.imap([1, 2, 3], lambda x: x * x)
    assert list(results) == [1, 4, 9]

# Test cases for imap_unordered method
def test_imap_unordered():
    pool = PoolWrapper()
    results = pool.imap_unordered([1, 2, 3], lambda x: x * x)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper___init___0.py F.  [100%]

=================================== FAILURES ===================================
__________________________________ test_imap ___________________________________

    def test_imap():
        pool = PoolWrapper()
        results = pool.imap([1, 2, 3], lambda x: x * x)
>       assert list(results) == [1, 4, 9]

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper___init___0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <multiprocessing.pool.IMapIterator object at 0x7ffb16ed0390>
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
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper___init___0.py::test_imap
========================= 1 failed, 1 passed in 0.40s ==========================

Exception ignored in: <function Pool.__del__ at 0x7ffb16c40e00>
Traceback (most recent call last):
  File "/usr/local/lib/python3.11/multiprocessing/pool.py", line 271, in __del__
    self._change_notifier.put(None)
  File "/usr/local/lib/python3.11/multiprocessing/queues.py", line 377, in put
    self._writer.send_bytes(obj)
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 200, in send_bytes
    self._send_bytes(m[offset:offset + size])
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 427, in _send_bytes
    self._send(header + buf)
  File "/usr/local/lib/python3.11/multiprocessing/connection.py", line 384, in _send
    n = write(self._handle, buf)
        ^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 9] Bad file descriptor
"""