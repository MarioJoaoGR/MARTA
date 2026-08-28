
import pytest
from youtube_dl.aes import xor

def test_xor_basic():
    result = xor([1, 0, 1], [0, 1, 0])
    assert result == [1, 1, 1]

def test_xor_different_values():
    result = xor([5, 3, 9], [4, 8, 1])
    assert result == [1, 11, 8]

def test_xor_empty_lists():
    result = xor([], [])
    assert result == []
