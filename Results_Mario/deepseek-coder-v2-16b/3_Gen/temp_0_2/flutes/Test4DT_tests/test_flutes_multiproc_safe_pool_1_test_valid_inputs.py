
import pytest
from flutes.multiproc import safe_pool
from multiprocessing import Pool, cpu_count

def square(x):
    return x * x

@pytest.mark.parametrize("processes", [1, 4])
def test_valid_inputs(processes):
    with safe_pool(processes=processes) as pool:
        results = pool.map(square, range(10))
        assert len(results) == 10
        for i in range(10):
            assert results[i] == i * i
