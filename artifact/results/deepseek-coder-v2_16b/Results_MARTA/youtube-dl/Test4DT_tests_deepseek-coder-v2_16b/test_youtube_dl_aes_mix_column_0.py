
import pytest
from youtube_dl.aes import mix_column

def test_mix_column_identity_matrix():
    assert mix_column([3, 4, 5, 6], [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == [3, 4, 5, 6]

def test_mix_column_constant_matrix():
    assert mix_column([1, 2, 3, 4], [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]) == [2, 4, 6, 8]

