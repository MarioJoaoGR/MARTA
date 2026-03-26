
import pytest
from pytutils.iters import dedupe

def test_valid_input():
    @dedupe
    def my_func():
        return [1, 2, 3, 2, 1]
    
    result = list(my_func())
    assert result == [1, 2, 3]
