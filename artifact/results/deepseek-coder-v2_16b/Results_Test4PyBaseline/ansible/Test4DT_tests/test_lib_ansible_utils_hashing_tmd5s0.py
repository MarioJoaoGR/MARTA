
import hashlib
import pytest
from ansible.utils.hashing import md5s

# Test cases for the md5s function
def test_md5s_string():
    # Test with a string input
    result = md5s("hello world")
    assert isinstance(result, str), "Expected a string output"
    assert len(result) == 32, "Expected MD5 hash length to be 32 characters"
    assert result == '5eb63bbbe01eeed093cb22bb8f5acdc3', f"Unexpected MD5 hash for 'hello world': {result}"

def test_md5s_bytes():
    # Test with bytes input
    result = md5s(b"hello world")
    assert isinstance(result, str), "Expected a string output"
    assert len(result) == 32, "Expected MD5 hash length to be 32 characters"