
import pytest
import os
from hashlib import sha1, md5
from unittest.mock import patch, MagicMock
from ansible.utils.hashing import secure_hash

# Test for valid input with a valid file path and default hash function
def test_valid_input():
    # Ensure a valid file exists at the specified path for hashing
    filename = 'testfile.txt'
    with open(filename, 'w') as f:
        f.write('test content')
    
    expected_hash = sha1('test content'.encode()).hexdigest()
    
    result = secure_hash(filename)
    
    assert result == expected_hash
    
    os.remove(filename)

# Test for invalid file (file does not exist or is a directory)
def test_invalid_file():
    # Create scenarios where the file path points to a non-existing file or a directory
    with patch('os.path.exists', return_value=False):
        assert secure_hash('non_existent_file') is None
    
    with patch('os.path.isdir', return_value=True):
        assert secure_hash('test_directory') is None

# Test for custom hash function provided as an argument
def test_custom_hash_function():
    # Implement and provide a mock custom hash function for testing
    def custom_hash(data):
        return sha1(data).hexdigest()
    
    with patch('ansible.utils.hashing.secure_hash', side_effect=custom_hash):
        filename = 'testfile.txt'
        with open(filename, 'w') as f:
            f.write('test content')
        
        result = secure_hash(filename)
        
        assert result == sha1('test content'.encode()).hexdigest()
        
        os.remove(filename)
