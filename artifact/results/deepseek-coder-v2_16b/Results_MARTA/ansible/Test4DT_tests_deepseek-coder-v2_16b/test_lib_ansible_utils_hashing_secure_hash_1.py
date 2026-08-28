
import os
from hashlib import sha1, md5
import pytest
from ansible.utils.hashing import secure_hash
from unittest.mock import patch

# Scenario 1: Test standard input with default SHA-1 hashing
def test_valid_input_default_sha1():
    # Ensure 'example.txt' exists in the current working directory
    open('example.txt', 'w').close()
    
    expected_hash = sha1(open('example.txt', 'rb').read()).hexdigest()
    assert secure_hash('example.txt') == expected_hash
    
    # Clean up
    os.remove('example.txt')

# Scenario 2: Test standard input with MD5 hashing
def test_valid_input_custom_md5():
    # Ensure 'example.txt' exists in the current working directory
    open('example.txt', 'w').close()
    
    def mock_md5(data):
        m = md5()
        m.update(data)
        return m
    
    with patch('ansible.utils.hashing.md5', side_effect=mock_md5):
        expected_hash = md5(open('example.txt', 'rb').read()).hexdigest()
        assert secure_hash('example.txt', hash_func=md5) == expected_hash
    
    # Clean up
    os.remove('example.txt')

# Scenario 3: Test invalid file path (non-existent file)
def test_invalid_file_path():
    # Create a non-existent file 'nonexistent.txt' in the current working directory
    with pytest.raises(IOError):
        secure_hash('nonexistent.txt')
