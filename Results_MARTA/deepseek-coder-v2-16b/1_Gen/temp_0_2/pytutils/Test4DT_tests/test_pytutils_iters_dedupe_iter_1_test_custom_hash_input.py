
import pytest
from pytutils.iters import dedupe_iter

def test_custom_hash_input():
    data = [12, 34, 56, 78, 34]
    def my_hash(x): return x % 10
    
    result = list(dedupe_iter(data, my_hash))
    assert result == [12, 34, 56, 78], f"Expected deduplicated list to be [12, 34, 56, 78], but got {result}"
