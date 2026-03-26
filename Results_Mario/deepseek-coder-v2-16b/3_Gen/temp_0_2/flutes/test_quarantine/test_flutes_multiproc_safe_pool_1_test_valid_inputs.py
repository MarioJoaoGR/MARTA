
import pytest
from multiprocessing import Pool
from flutes.multiproc import safe_pool

@pytest.mark.parametrize("processes", [1, 4])
def test_valid_inputs(processes):
    def square(x):
        return x * x
    
    with safe_pool(processes=processes) as pool:
        results = pool.map(square, range(10))
        assert len(results) == 10
        for i in range(10):
            assert results[i] == i ** 2

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

flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_valid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_inputs[1] _____________________________

processes = 1

    @pytest.mark.parametrize("processes", [1, 4])
    def test_valid_inputs(processes):
        def square(x):
            return x * x
    
        with safe_pool(processes=processes) as pool:
>           results = pool.map(square, range(10))

flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_valid_inputs.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:264: in wrapped_method
    return pool_method(func, *_, **__)
/usr/local/lib/python3.11/multiprocessing/pool.py:367: in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
/usr/local/lib/python3.11/multiprocessing/pool.py:774: in get
    raise self._value
/usr/local/lib/python3.11/multiprocessing/pool.py:540: in _handle_tasks
    put(task)
/usr/local/lib/python3.11/multiprocessing/connection.py:206: in send
    self._send_bytes(_ForkingPickler.dumps(obj))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'multiprocessing.reduction.ForkingPickler'>
obj = (0, 0, <function mapstar at 0x7f9d516a1e40>, ((<function test_valid_inputs.<locals>.square at 0x7f9d516611c0>, (0, 1, 2)),), {})
protocol = None

    @classmethod
    def dumps(cls, obj, protocol=None):
        buf = io.BytesIO()
>       cls(buf, protocol).dump(obj)
E       AttributeError: Can't pickle local object 'test_valid_inputs.<locals>.square'

/usr/local/lib/python3.11/multiprocessing/reduction.py:51: AttributeError
_____________________________ test_valid_inputs[4] _____________________________

processes = 4

    @pytest.mark.parametrize("processes", [1, 4])
    def test_valid_inputs(processes):
        def square(x):
            return x * x
    
        with safe_pool(processes=processes) as pool:
>           results = pool.map(square, range(10))

flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_valid_inputs.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:264: in wrapped_method
    return pool_method(func, *_, **__)
/usr/local/lib/python3.11/multiprocessing/pool.py:367: in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
/usr/local/lib/python3.11/multiprocessing/pool.py:774: in get
    raise self._value
/usr/local/lib/python3.11/multiprocessing/pool.py:540: in _handle_tasks
    put(task)
/usr/local/lib/python3.11/multiprocessing/connection.py:206: in send
    self._send_bytes(_ForkingPickler.dumps(obj))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'multiprocessing.reduction.ForkingPickler'>
obj = (1, 0, <function mapstar at 0x7f9d516a1e40>, ((<function test_valid_inputs.<locals>.square at 0x7f9d5173e660>, (0,)),), {})
protocol = None

    @classmethod
    def dumps(cls, obj, protocol=None):
        buf = io.BytesIO()
>       cls(buf, protocol).dump(obj)
E       AttributeError: Can't pickle local object 'test_valid_inputs.<locals>.square'

/usr/local/lib/python3.11/multiprocessing/reduction.py:51: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_valid_inputs.py::test_valid_inputs[1]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_valid_inputs.py::test_valid_inputs[4]
============================== 2 failed in 0.23s ===============================
"""