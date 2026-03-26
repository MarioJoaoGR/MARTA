
import pytest
from flutes.multiproc import PoolWrapper

@pytest.fixture
def pool_wrapper():
    return PoolWrapper()

def test_imap(pool_wrapper):
    result = list(pool_wrapper.imap([1, 2, 3], lambda x: x * x))
    assert result == [1, 4, 9]

def test_imap_unordered(pool_wrapper):
    result = list(pool_wrapper.imap_unordered([1, 2, 3], lambda x: x * x))
    assert set(result) == {1, 4, 9}

def test_map(pool_wrapper):
    result = list(pool_wrapper.map([1, 2, 3], lambda x: x * x))
    assert result == [1, 4, 9]

def test_map_async(pool_wrapper):
    async_result = pool_wrapper.map_async([1, 2, 3], lambda x: x * x)
    # Assuming map_async returns an asynchronous result object that can be checked later
    assert async_result is not None

def test_starmap(pool_wrapper):
    result = list(pool_wrapper.starmap([(1,), (2,), (3,)], lambda x: x * x))
    assert result == [1, 4, 9]

def test_starmap_async(pool_wrapper):
    async_result = pool_wrapper.starmap_async([(1,), (2,), (3,)], lambda x: x * x)
    # Assuming starmap_async returns an asynchronous result object that can be checked later
    assert async_result is not None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py F [ 16%]
FFFFF                                                                    [100%]

=================================== FAILURES ===================================
__________________________________ test_imap ___________________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_imap(pool_wrapper):
>       result = list(pool_wrapper.imap([1, 2, 3], lambda x: x * x))

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <multiprocessing.pool.IMapIterator object at 0x7f48cb66c290>
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
_____________________________ test_imap_unordered ______________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_imap_unordered(pool_wrapper):
>       result = list(pool_wrapper.imap_unordered([1, 2, 3], lambda x: x * x))

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <multiprocessing.pool.IMapUnorderedIterator object at 0x7f48cb3a2b90>
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
___________________________________ test_map ___________________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_map(pool_wrapper):
>       result = list(pool_wrapper.map([1, 2, 3], lambda x: x * x))

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:264: in wrapped_method
    return pool_method(func, *_, **__)
/usr/local/lib/python3.11/multiprocessing/pool.py:367: in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>, func = [1, 2, 3]
iterable = <function test_map.<locals>.<lambda> at 0x7f48cb1e2f20>
mapper = <function mapstar at 0x7f48cb61cae0>, chunksize = None, callback = None
error_callback = None

    def _map_async(self, func, iterable, mapper, chunksize=None, callback=None,
            error_callback=None):
        '''
        Helper function to implement map, starmap and their async counterparts.
        '''
        self._check_running()
        if not hasattr(iterable, '__len__'):
>           iterable = list(iterable)
E           TypeError: 'function' object is not iterable

/usr/local/lib/python3.11/multiprocessing/pool.py:478: TypeError
________________________________ test_map_async ________________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_map_async(pool_wrapper):
>       async_result = pool_wrapper.map_async([1, 2, 3], lambda x: x * x)

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:264: in wrapped_method
    return pool_method(func, *_, **__)
/usr/local/lib/python3.11/multiprocessing/pool.py:468: in map_async
    return self._map_async(func, iterable, mapstar, chunksize, callback,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>, func = [1, 2, 3]
iterable = <function test_map_async.<locals>.<lambda> at 0x7f48cb43e3e0>
mapper = <function mapstar at 0x7f48cb61cae0>, chunksize = None, callback = None
error_callback = None

    def _map_async(self, func, iterable, mapper, chunksize=None, callback=None,
            error_callback=None):
        '''
        Helper function to implement map, starmap and their async counterparts.
        '''
        self._check_running()
        if not hasattr(iterable, '__len__'):
>           iterable = list(iterable)
E           TypeError: 'function' object is not iterable

/usr/local/lib/python3.11/multiprocessing/pool.py:478: TypeError
_________________________________ test_starmap _________________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_starmap(pool_wrapper):
>       result = list(pool_wrapper.starmap([(1,), (2,), (3,)], lambda x: x * x))

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:264: in wrapped_method
    return pool_method(func, *_, **__)
/usr/local/lib/python3.11/multiprocessing/pool.py:375: in starmap
    return self._map_async(func, iterable, starmapstar, chunksize).get()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>
func = [(1,), (2,), (3,)]
iterable = <function test_starmap.<locals>.<lambda> at 0x7f48cb1e2de0>
mapper = <function starmapstar at 0x7f48cb61d1c0>, chunksize = None
callback = None, error_callback = None

    def _map_async(self, func, iterable, mapper, chunksize=None, callback=None,
            error_callback=None):
        '''
        Helper function to implement map, starmap and their async counterparts.
        '''
        self._check_running()
        if not hasattr(iterable, '__len__'):
>           iterable = list(iterable)
E           TypeError: 'function' object is not iterable

/usr/local/lib/python3.11/multiprocessing/pool.py:478: TypeError
______________________________ test_starmap_async ______________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_starmap_async(pool_wrapper):
>       async_result = pool_wrapper.starmap_async([(1,), (2,), (3,)], lambda x: x * x)

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:264: in wrapped_method
    return pool_method(func, *_, **__)
/usr/local/lib/python3.11/multiprocessing/pool.py:382: in starmap_async
    return self._map_async(func, iterable, starmapstar, chunksize,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>
func = [(1,), (2,), (3,)]
iterable = <function test_starmap_async.<locals>.<lambda> at 0x7f48cb1e28e0>
mapper = <function starmapstar at 0x7f48cb61d1c0>, chunksize = None
callback = None, error_callback = None

    def _map_async(self, func, iterable, mapper, chunksize=None, callback=None,
            error_callback=None):
        '''
        Helper function to implement map, starmap and their async counterparts.
        '''
        self._check_running()
        if not hasattr(iterable, '__len__'):
>           iterable = list(iterable)
E           TypeError: 'function' object is not iterable

/usr/local/lib/python3.11/multiprocessing/pool.py:478: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_imap
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_imap_unordered
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_map
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_map_async
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_starmap
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_starmap_async
============================== 6 failed in 1.94s ===============================

Exception ignored in: <function Pool.__del__ at 0x7f48cb61fd80>
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
Exception ignored in: <function Pool.__del__ at 0x7f48cb61fd80>
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
Exception ignored in: <function Pool.__del__ at 0x7f48cb61fd80>
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