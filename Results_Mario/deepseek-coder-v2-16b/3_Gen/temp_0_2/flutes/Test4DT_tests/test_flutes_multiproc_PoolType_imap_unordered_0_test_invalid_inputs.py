
import pytest
from flutes.multiproc import PoolType
from typing import Callable, Iterable, Iterator, Any, Mapping

def square(x):
    return x ** 2

@pytest.mark.parametrize("fn, iterable, chunksize, args, kwds", [
    (None, range(10), 1, (), {}),
    (square, None, 1, (), {}),
    (square, range(10), -1, (), {}),
    (square, range(10), 1, "invalid_args", {}),
    (square, range(10), 1, (1, 2, 3), {"extra": "kwds"}),
])
def test_invalid_inputs(fn, iterable, chunksize, args, kwds):
    pool = PoolType()
    with pytest.raises(TypeError):
        list(pool.imap_unordered(fn, iterable, chunksize, args=args, kwds=kwds))
