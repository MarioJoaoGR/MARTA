
import pytest
from multiprocessing import Pool
from flutes.multiproc import PoolType

def multiply(a, b):
    return a * b

@pytest.mark.parametrize("fn, iterable, chunksize, args, kwds", [
    (multiply, [(2, 3), (4, 5)], None, (), {}),
    (multiply, [(1, 2), (3, 4)], 1, (), {}),
])
def test_invalid_input(fn, iterable, chunksize, args, kwds):
    pool = PoolType()
    with pytest.raises(TypeError):
        results = pool.starmap(fn, iterable, chunksize, args=args, kwds=kwds)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_starmap_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0_test_invalid_input.py:16:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)

"""