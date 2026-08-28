# Module: ansible.executor.discovery.python_target
import pytest
import os
import io
from ansible.executor.discovery.python_target import read_utf8_file

# Test reading a valid UTF-8 encoded file
def test_read_valid_utf8_file():
    # Create a temporary file with UTF-8 content
    temp_file_path = 'temp_test_file.txt'
    with open(temp_file_path, 'w', encoding='utf-8') as f:
        f.write('Hello, world!')
    
    # Read the file and check its content
    result = read_utf8_file(temp_file_path)
    assert result == 'Hello, world!'
    
    # Clean up the temporary file
    os.remove(temp_file_path)

# Test reading a non-existent file
def test_read_non_existent_file():
    # Try to read a non-existent file and check it returns None
    result = read_utf8_file('nonexistent_file.txt')
    assert result is None

# Test reading a file with a different encoding
def test_read_file_with_different_encoding():
    # Create a temporary file with ISO-8859-1 content
    temp_file_path = 'temp_test_file.txt'
    with open(temp_file_path, 'w', encoding='ISO-8859-1') as f:
        f.write('Hello, world!')
    
    # Read the file with UTF-8 encoding and check its content
    result = read_utf8_file(temp_file_path, 'ISO-8859-1')
    assert result == 'Hello, world!'
    
    # Clean up the temporary file
    os.remove(temp_file_path)

# Test reading a file without read permissions
def test_read_file_without_permissions():
    # Create a temporary file with write permissions only
    temp_file_path = 'temp_test_file.txt'
    with open(temp_file_path, 'w') as f:
        f.write('Hello, world!')
    
    # Try to read the file without read permissions and check it returns None
    os.chmod(temp_file_path, 0o222)  # Set write-only permissions
    result = read_utf8_file(temp_file_path)
    assert result is None
    
    # Clean up the temporary file
    os.remove(temp_file_path)
