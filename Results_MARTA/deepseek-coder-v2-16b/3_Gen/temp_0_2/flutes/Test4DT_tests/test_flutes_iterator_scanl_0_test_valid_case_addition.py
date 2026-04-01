
import pytest
from flutes.iterator import scanl

def test_valid_case_addition():
    func = lambda x, y: x + y
    iterable = [1, 2, 3, 4]
    
    result = list(scanl(func, iterable))
    assert result == [1, 3, 6, 10]
