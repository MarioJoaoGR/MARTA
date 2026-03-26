
import pytest
from flutes.iterator import scanl

def add(x, y):
    return x + y

def test_valid_case():
    result = list(scanl(add, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]
