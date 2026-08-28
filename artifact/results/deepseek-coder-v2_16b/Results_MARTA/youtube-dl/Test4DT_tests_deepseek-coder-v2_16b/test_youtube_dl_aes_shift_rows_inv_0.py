
import pytest
from youtube_dl.aes import shift_rows_inv

def test_valid_case():
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    expected_output = [0, 13, 10, 7, 4, 1, 14, 11, 8, 5, 2, 15, 12, 9, 6, 3]
    assert shift_rows_inv(data) == expected_output

def test_edge_case():
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    expected_output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert shift_rows_inv(data) == expected_output

def test_invalid_input():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    with pytest.raises(IndexError):
        shift_rows_inv(data)
