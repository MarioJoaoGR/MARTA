
import pytest
from flutes.multiproc import DummyPool

def test_valid_inputs():
    def square(x):
        return x ** 2
    
    numbers = [1, 2, 3, 4]
    pool = DummyPool(processes=0)
    result_iter = pool.imap_unordered(square, numbers)
    
    results = list(result_iter)
    
    assert len(results) == len(numbers)
    for num, res in zip(numbers, results):
        assert res == square(num)
