
import pytest
from ansible.utils.hashing import md5s

def test_valid_input():
    # Test case for valid input string
    result = md5s("hello world")
    assert isinstance(result, str), "Expected a string output"
    assert len(result) == 32, "Expected MD5 hash length to be 32 characters"
    assert result == '5eb63bbbe01eeed093cb22bb8f5acdc3', "MD5 hash does not match expected value"

    # Test case for valid input bytes
    result_bytes = md5s(b"hello world")
    assert isinstance(result_bytes, str), "Expected a string output"
    assert len(result_bytes) == 32, "Expected MD5 hash length to be 32 characters"
    assert result_bytes == '5eb63bbbe01eeed093cb22bb8f5acdc3', "MD5 hash does not match expected value"
