
import pytest
from youtube_dl.aes import sub_bytes_inv, SBOX_INV


def test_valid_byte_values():
    data = [0, 255]
    expected_output = [SBOX_INV[0], SBOX_INV[255]]
    assert sub_bytes_inv(data) == expected_output

def test_large_list():
    data = [100, 150, 200, 250]
    expected_output = [SBOX_INV[100], SBOX_INV[150], SBOX_INV[200], SBOX_INV[250]]
    assert sub_bytes_inv(data) == expected_output

def test_edge_case_min():
    data = [0]
    expected_output = [SBOX_INV[0]]
    assert sub_bytes_inv(data) == expected_output

def test_edge_case_max():
    data = [255]
    expected_output = [SBOX_INV[255]]
    assert sub_bytes_inv(data) == expected_output