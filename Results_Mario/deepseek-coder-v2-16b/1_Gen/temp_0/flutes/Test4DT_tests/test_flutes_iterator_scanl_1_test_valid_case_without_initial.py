
import pytest
from operator import add
from flutes.iterator import scanl

def test_valid_case_without_initial():
    result = list(scanl(add, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]
