
import pytest
import hashlib
from ansible.plugins.filter import core

# Test cases for get_hash function
def test_get_hash_default_sha1():
    result = core.get_hash('hello')
    assert result == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'

def test_get_hash_md5():
    result = core.get_hash('hello', hashtype='md5')
    assert result == '5d41402abc4b2a76b9719d911017c592'

def test_get_hash_sha256():
    result = core.get_hash('hello', hashtype='sha256')
    assert result == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'

def test_get_hash_custom_data():
    result = core.get_hash(b'world', hashtype='sha1')
    assert result == '2aae6c35c94fcfb415dbe95f7fd0f5e48ebf0acaef1780b5'

def test_get_hash_custom_data_md5():
    result = core.get_hash(b'example data', hashtype='md5')
    assert result == '9a2ae3f6ec4e2d9c78ff041eefafb2a8'

def test_get_hash_custom_data_sha256():
    result = core.get_hash(b'another example', hashtype='sha256')
    assert result == 'ba3253876aed6bc2d1fae9aa4ae4c0a2'
