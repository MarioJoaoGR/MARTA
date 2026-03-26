
import pytest
from flutes.multiproc import PoolType

@pytest.mark.parametrize("fn, iterable, chunksize, args, kwds", [
    (lambda x: x ** 2, [1, 2, 3, 4], None, (), {})
])
def test_map(fn, iterable, chunksize, args, kwds):
    pool = PoolType()
    result = pool.map(fn, iterable, chunksize, *args, **kwds)
    assert result == [1, 4, 9, 16]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_PoolType_map_0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_0_test_edge_case.py:10:4: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)


"""