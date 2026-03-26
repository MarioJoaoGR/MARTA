
import pytest
from flutes.multiproc import PoolType
from typing import Callable, Iterator, Iterable, Any, Mapping

def example_fn(x):
    yield x * 2
    yield x * 3

@pytest.mark.parametrize("chunksize", [0, -1])
def test_invalid_input(chunksize):
    pool = PoolType()
    with pytest.raises(ValueError):
        list(pool.gather(example_fn, [1, 2, 3], chunksize=chunksize))

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_input[0] _____________________________

chunksize = 0

    @pytest.mark.parametrize("chunksize", [0, -1])
    def test_invalid_input(chunksize):
        pool = PoolType()
        with pytest.raises(ValueError):
>           list(pool.gather(example_fn, [1, 2, 3], chunksize=chunksize))
E           TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_invalid_input.py:14: TypeError
____________________________ test_invalid_input[-1] ____________________________

chunksize = -1

    @pytest.mark.parametrize("chunksize", [0, -1])
    def test_invalid_input(chunksize):
        pool = PoolType()
        with pytest.raises(ValueError):
>           list(pool.gather(example_fn, [1, 2, 3], chunksize=chunksize))
E           TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_invalid_input.py:14: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_invalid_input.py::test_invalid_input[0]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_invalid_input.py::test_invalid_input[-1]
============================== 2 failed in 0.33s ===============================
"""