
import pytest
from ansible.utils.hashing import md5s

def test_md5s_valid_input():
    # Test valid string input
    data = "hello world"
    expected_hash = '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert md5s(data) == expected_hash

    # Test valid bytes input
    data_bytes = b"hello world"
    assert md5s(data_bytes) == expected_hash
