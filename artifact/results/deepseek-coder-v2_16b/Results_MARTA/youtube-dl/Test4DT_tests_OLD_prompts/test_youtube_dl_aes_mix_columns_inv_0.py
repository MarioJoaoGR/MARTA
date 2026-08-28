
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.aes import mix_columns_inv

def test_mix_columns_inv_default_matrix():
    with patch('youtube_dl.aes.MIX_COLUMN_MATRIX_INV', [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]):
        result = mix_columns_inv([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        assert result == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def test_mix_columns_inv_custom_matrix():
    custom_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    with patch('youtube_dl.aes.MIX_COLUMN_MATRIX_INV', custom_matrix):
        result = mix_columns_inv([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        assert result == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def test_mix_columns_inv_incorrect_data_type():
    with pytest.raises(TypeError):
        mix_columns_inv("incorrect_data_type")

def test_mix_columns_inv_incorrect_matrix_type():
    with pytest.raises(TypeError):
        mix_columns_inv([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "incorrect_matrix_type")
