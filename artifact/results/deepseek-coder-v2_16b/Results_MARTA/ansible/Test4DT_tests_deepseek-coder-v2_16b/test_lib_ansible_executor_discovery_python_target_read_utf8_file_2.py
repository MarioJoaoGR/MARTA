
import pytest
import os
import io
from ansible.executor.discovery.python_target import read_utf8_file

def test_read_valid_utf8_file():
    # Create a temporary file with valid UTF-8 content
    temp_file_path = '/tmp/test_file.txt'
    with open(temp_file_path, 'w', encoding='utf-8') as f:
        f.write('Hello, world!')
    
    # Read the file and assert its content
    content = read_utf8_file(temp_file_path)
    assert content == 'Hello, world!'
    
    # Clean up the temporary file
    os.remove(temp_file_path)
