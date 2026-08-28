
import pytest
from unittest.mock import patch
from youtube_dl.aes import mix_columns, MIX_COLUMN_MATRIX


def test_mix_columns_custom_matrix():
    data = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    custom_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    result = mix_columns(data, custom_matrix)
    assert result == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]