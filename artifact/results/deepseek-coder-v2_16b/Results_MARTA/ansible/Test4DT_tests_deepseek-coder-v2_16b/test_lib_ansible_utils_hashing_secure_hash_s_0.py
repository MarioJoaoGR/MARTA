
import pytest
import hashlib
from ansible.utils.hashing import secure_hash_s

def custom_hash(data):
    return hashlib.sha256(data).hexdigest()

def test_secure_hash_s_with_default_hash():
    result = secure_hash_s("hello world")
    assert result == hashlib.sha1("hello world".encode()).hexdigest()


def test_secure_hash_s_with_default_hash_bytes():
    result = secure_hash_s(b"hello world")
    assert result == hashlib.sha1(b"hello world").hexdigest()