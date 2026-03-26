
import pytest
from flutes.multiproc import PoolType
from typing import Callable, Iterable, Iterator, Any, Mapping

# Define a dummy function to use in the test
def square(x: int) -> int:
    return x ** 2

@pytest.fixture
def pool():
    return PoolType()

def test_invalid_inputs(pool):
    with pytest.raises(TypeError):
        # Test when fn is not a callable
        result_iter = pool.imap_unordered("not_a_function", [1, 2, 3])
    
    with pytest.raises(TypeError):
        # Test when iterable is not an iterable
        result_iter = pool.imap_unordered(square, "not_an_iterable")
    
    with pytest.raises(TypeError):
        # Test when chunksize is not an integer
        result_iter = pool.imap_unordered(square, [1, 2, 3], chunksize="not_an_integer")
    
    with pytest.raises(TypeError):
        # Test when args is not an iterable of any
        result_iter = pool.imap_unordered(square, [1, 2, 3], chunksize=1, args="not_an_iterable")
    
    with pytest.raises(TypeError):
        # Test when kwds is not a mapping of string to any
        result_iter = pool.imap_unordered(square, [1, 2, 3], chunksize=1, kwds="not_a_mapping")

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_invalid_inputs(pool):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_invalid_inputs.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.20s ===============================
"""