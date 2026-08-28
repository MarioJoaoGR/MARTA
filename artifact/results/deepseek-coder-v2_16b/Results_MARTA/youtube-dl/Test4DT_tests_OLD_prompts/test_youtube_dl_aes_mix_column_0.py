
import pytest
from unittest.mock import patch
from youtube_dl.aes import mix_column

def test_mix_column_identity_matrix():
    data = [3, 4, 5, 6]
    matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    result = mix_column(data, matrix)
    assert result == [3, 4, 5, 6]

def test_mix_column_constant_matrix():
    data = [1, 2, 3, 4]
    matrix = [[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]
    result = mix_column(data, matrix)
    assert result == [2, 4, 6, 8]
