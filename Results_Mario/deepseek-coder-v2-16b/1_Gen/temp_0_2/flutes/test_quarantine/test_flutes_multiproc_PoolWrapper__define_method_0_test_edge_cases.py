
import pytest
from flutes.multiproc import PoolWrapper

@pytest.fixture
def pool_wrapper():
    return PoolWrapper()

def test_starmap(pool_wrapper):
    results = list(pool_wrapper.starmap(lambda x: x * x, [(1,), (2,), (3,), (4,)]))
    assert results == [1, 4, 9, 16]

def test_starmap_async(pool_wrapper):
    from multiprocessing import Pool as MPool
    pool = MPool()
    async_result = pool.starmap_async(lambda x: x * x, [(1,), (2,), (3,), (4,)])
    results = list(async_result.get())
    assert results == [1, 4, 9, 16]

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________________ test_starmap _________________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_starmap(pool_wrapper):
>       results = list(pool_wrapper.starmap(lambda x: x * x, [(1,), (2,), (3,), (4,)]))

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:264: in wrapped_method
    return pool_method(func, *_, **__)
/usr/local/lib/python3.11/multiprocessing/pool.py:375: in starmap
    return self._map_async(func, iterable, starmapstar, chunksize).get()
/usr/local/lib/python3.11/multiprocessing/pool.py:774: in get
    raise self._value
/usr/local/lib/python3.11/multiprocessing/pool.py:540: in _handle_tasks
    put(task)
/usr/local/lib/python3.11/multiprocessing/connection.py:206: in send
    self._send_bytes(_ForkingPickler.dumps(obj))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'multiprocessing.reduction.ForkingPickler'>
obj = (0, 0, <function starmapstar at 0x7fcc294e1da0>, ((<function test_starmap.<locals>.<lambda> at 0x7fcc29302160>, ((1,),)),), {})
protocol = None

    @classmethod
    def dumps(cls, obj, protocol=None):
        buf = io.BytesIO()
>       cls(buf, protocol).dump(obj)
E       AttributeError: Can't pickle local object 'test_starmap.<locals>.<lambda>'

/usr/local/lib/python3.11/multiprocessing/reduction.py:51: AttributeError
______________________________ test_starmap_async ______________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_starmap_async(pool_wrapper):
        from multiprocessing import Pool as MPool
        pool = MPool()
        async_result = pool.starmap_async(lambda x: x * x, [(1,), (2,), (3,), (4,)])
>       results = list(async_result.get())

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/multiprocessing/pool.py:774: in get
    raise self._value
/usr/local/lib/python3.11/multiprocessing/pool.py:540: in _handle_tasks
    put(task)
/usr/local/lib/python3.11/multiprocessing/connection.py:206: in send
    self._send_bytes(_ForkingPickler.dumps(obj))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'multiprocessing.reduction.ForkingPickler'>
obj = (1, 0, <function starmapstar at 0x7fcc294e1da0>, ((<function test_starmap_async.<locals>.<lambda> at 0x7fcc29279da0>, ((1,),)),), {})
protocol = None

    @classmethod
    def dumps(cls, obj, protocol=None):
        buf = io.BytesIO()
>       cls(buf, protocol).dump(obj)
E       AttributeError: Can't pickle local object 'test_starmap_async.<locals>.<lambda>'

/usr/local/lib/python3.11/multiprocessing/reduction.py:51: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_starmap
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_starmap_async
============================== 2 failed in 0.77s ===============================

Exception ignored in: <function Pool.__del__ at 0x7fcc294d49a0>
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