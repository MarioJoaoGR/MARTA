
import pytest
from flutes.multiproc import PoolWrapper
from multiprocessing import Pool, pool

def square(x):
    return x * x

@pytest.fixture
def pool_wrapper():
    return PoolWrapper()

def test_valid_inputs(pool_wrapper):
    # Test map method with a function and valid arguments
    results = pool_wrapper.map(square, [1, 2, 3, 4])
    assert results == [1, 4, 9, 16]

    # Test imap method with a function and valid arguments
    results = list(pool_wrapper.imap(square, [1, 2, 3, 4]))
    assert results == [1, 4, 9, 16]

    # Test map_async method with a function and valid arguments
    async_result = pool_wrapper.map_async(square, [1, 2, 3, 4])
    results = async_result.get()
    assert results == [1, 4, 9, 16]

    # Test starmap method with a function and valid arguments
    results = pool_wrapper.starmap(lambda x: x * x, [(1,), (2,), (3,)])
    assert results == [1, 4, 9]

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

pool_wrapper = <flutes.multiproc.PoolWrapper state=RUN pool_size=128>

    def test_valid_inputs(pool_wrapper):
        # Test map method with a function and valid arguments
        results = pool_wrapper.map(square, [1, 2, 3, 4])
        assert results == [1, 4, 9, 16]
    
        # Test imap method with a function and valid arguments
        results = list(pool_wrapper.imap(square, [1, 2, 3, 4]))
        assert results == [1, 4, 9, 16]
    
        # Test map_async method with a function and valid arguments
        async_result = pool_wrapper.map_async(square, [1, 2, 3, 4])
        results = async_result.get()
        assert results == [1, 4, 9, 16]
    
        # Test starmap method with a function and valid arguments
>       results = pool_wrapper.starmap(lambda x: x * x, [(1,), (2,), (3,)])

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py:28: 
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
obj = (3, 0, <function starmapstar at 0x7f53a7e336a0>, ((<function test_valid_inputs.<locals>.<lambda> at 0x7f53a7e13920>, ((1,),)),), {})
protocol = None

    @classmethod
    def dumps(cls, obj, protocol=None):
        buf = io.BytesIO()
>       cls(buf, protocol).dump(obj)
E       AttributeError: Can't pickle local object 'test_valid_inputs.<locals>.<lambda>'

/usr/local/lib/python3.11/multiprocessing/reduction.py:51: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.24s ===============================
"""