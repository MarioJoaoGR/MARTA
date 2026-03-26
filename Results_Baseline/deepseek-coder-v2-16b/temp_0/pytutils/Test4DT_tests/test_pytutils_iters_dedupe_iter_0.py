
import pytest
from itertools import repeat, cycle
from pytutils.iters import dedupe_iter

def test_dedupe_iter_default_hash():
    result = dedupe_iter([1, 2, 3, 2, 1])
    assert list(result) == [1, 2, 3]

def test_dedupe_iter_custom_hash():
    def custom_hash(x):
        return x % 10
    result = dedupe_iter([11, 21, 31, 21, 11], custom_hash)