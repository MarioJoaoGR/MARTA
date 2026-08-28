
import pytest
import hashlib
from ansible.utils.hashing import secure_hash_s

# Helper function to convert string to bytes with error handling
def to_bytes(data, errors='surrogate_or_strict'):
    if isinstance(data, str):
        return data.encode('utf-8')
    elif isinstance(data, (bytes, bytearray)):
        return bytes(data)
    else:
        raise TypeError("Input should be a string or bytes")

# Test cases for secure_hash_s function
def test_secure_hash_s_default():
    result = secure_hash_s("hello world")
    assert isinstance(result, str), "Expected a string"
    assert len(result) == 40, "Expected SHA1 hash length to be 40 characters"
    assert result == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d', f"SHA1 hash of 'hello world' should match the expected value, but got {result}"

def test_secure_hash_s_sha256():
    result = secure_hash_s("hello world", hash_func=hashlib.sha256)
    assert isinstance(result, str), "Expected a string"
    assert len(result) == 64, "Expected SHA256 hash length to be 64 characters"
    assert result == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad', f"SHA256 hash of 'hello world' should match the expected value, but got {result}"

def test_secure_hash_s_custom_lambda():
    custom_sha1 = lambda: hashlib.sha1()
    result = secure_hash_s("hello world", hash_func=custom_sha1)
    assert isinstance(result, str), "Expected a string"
    assert len(result) == 40, "Expected SHA1 hash length to be 40 characters"
    assert result == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d', f"SHA1 hash of 'hello world' should match the expected value, but got {result}"

def test_secure_hash_s_empty():
    result = secure_hash_s("")
    assert isinstance(result, str), "Expected a string"
    assert len(result) == 40, "Expected SHA1 hash length to be 40 characters"
    assert result == 'da39a3ee5e6b4b0d3255bfef95601890afd80709', f"SHA1 hash of empty string should match the expected value, but got {result}"

def test_secure_hash_s_non_string():
    with pytest.raises(TypeError):
        secure_hash_s(b'hello world')  # Should raise TypeError as it expects a str
