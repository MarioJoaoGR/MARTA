
import pytest
from multiprocessing import Pool
from flutes.multiproc import PoolWrapper

def square(x):
    return x * x

@pytest.fixture
def pool_wrapper():
    return PoolWrapper()

def test_map(pool_wrapper):
    results = pool_wrapper.map(square, [1, 2, 3, 4])
    assert results == [1, 4, 9, 16]

def test_imap(pool_wrapper):
    with pytest.raises(NotImplementedError):
        pool_wrapper.imap(square, [1, 2, 3, 4])

def test_map_async(pool_wrapper):
    results = pool_wrapper.map_async(square, [1, 2, 3, 4]).get()
    assert results == [1, 4, 9, 16]

def test_starmap(pool_wrapper):
    with pytest.raises(NotImplementedError):
        pool_wrapper.starmap(lambda x: x * x, [(1,), (2,), (3,)])

def test_starmap_async(pool_wrapper):
    results = pool_wrapper.starmap_async(lambda x: x * x, [(1,), (2,), (3,)]).get()
    assert results == [1, 4, 9]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py . [ 20%]
F.FF                                                                     [100%]

=================================== FAILURES ===================================
__________________________________ test_imap ___________________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_imap(pool_wrapper):
>       with pytest.raises(NotImplementedError):
E       Failed: DID NOT RAISE <class 'NotImplementedError'>

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:18: Failed
_________________________________ test_starmap _________________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_starmap(pool_wrapper):
        with pytest.raises(NotImplementedError):
>           pool_wrapper.starmap(lambda x: x * x, [(1,), (2,), (3,)])

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:27: 
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
obj = (3, 0, <function starmapstar at 0x7f98e58c6d40>, ((<function test_starmap.<locals>.<lambda> at 0x7f98e5cbc4a0>, ((1,),)),), {})
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
>       results = pool_wrapper.starmap_async(lambda x: x * x, [(1,), (2,), (3,)]).get()

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/multiprocessing/pool.py:774: in get
    raise self._value
/usr/local/lib/python3.11/multiprocessing/pool.py:540: in _handle_tasks
    put(task)
/usr/local/lib/python3.11/multiprocessing/connection.py:206: in send
    self._send_bytes(_ForkingPickler.dumps(obj))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'multiprocessing.reduction.ForkingPickler'>
obj = (4, 0, <function starmapstar at 0x7f98e58c6d40>, ((<function test_starmap_async.<locals>.<lambda> at 0x7f98e5ab45e0>, ((1,),)),), {})
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
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_imap
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_starmap
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_edge_cases.py::test_starmap_async
========================= 3 failed, 2 passed in 1.25s ==========================

"""