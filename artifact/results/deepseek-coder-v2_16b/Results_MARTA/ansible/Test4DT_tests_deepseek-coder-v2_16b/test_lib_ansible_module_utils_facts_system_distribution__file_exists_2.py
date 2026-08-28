
import pytest
import os
from ansible.module_utils.facts.system.distribution import _file_exists

def test_valid_file():
    valid_path = '/tmp/existing_file.txt'
    with open(valid_path, 'w') as f:
        f.write('test content')
    
    assert _file_exists(valid_path) is True
    os.remove(valid_path)

def test_invalid_file():
    invalid_path = '/nonexistent_file'
    assert _file_exists(invalid_path) is False

def test_empty_file_with_allow_empty():
    empty_path = '/tmp/empty_file.txt'
    with open(empty_path, 'w') as f:
        pass
    
    assert _file_exists(empty_path, allow_empty=True) is True
    os.remove(empty_path)

def test_non_empty_file():
    non_empty_path = '/tmp/non_empty_file.txt'
    with open(non_empty_path, 'w') as f:
        f.write('some content')
    
    assert _file_exists(non_empty_path) is True
    os.remove(non_empty_path)
