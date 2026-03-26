
import pytest
from multiprocessing import Pool
from typing import Iterator, Callable, Iterable, Any, Mapping
from flutes.multiproc import PoolType

def test_error_case():
    pool = PoolType()
    
    def invalid_fn(x):
        return 'not an iterator'
    
    iterable = [1, 2, 3]
    
    with pytest.raises(TypeError):
        results = list(pool.gather(invalid_fn, iterable))
