
import pytest
from ansible.module_utils.facts.utils import get_file_content
import os
import fcntl

def test_get_file_content_existing_file():
    # Test reading a file that exists with default strip=True
    content = "Hello, World!"
    with open('test_file.txt', 'w') as f:
        f.write(content)
    
    assert get_file_content('test_file.txt') == content.strip()
    os.remove('test_file.txt')

def test_get_file_content_non_existent_file():
    # Test reading a file that does not exist with default strip=True
    assert get_file_content('nonexistent.txt', default='Default Content') == 'Default Content'

def test_get_file_content_empty_file():
    # Test reading an empty file with default strip=True
    with open('test_file.txt', 'w') as f:
        pass
    
    assert get_file_content('test_file.txt') is None
    os.remove('test_file.txt')

def test_get_file_content_stripped():
    # Test reading a file with content and ensuring it gets stripped
    content = " Hello, World! "
    with open('test_file.txt', 'w') as f:
        f.write(content)
    
    assert get_file_content('test_file.txt') == content.strip()
    os.remove('test_file.txt')

def test_get_file_content_not_stripped():
    # Test reading a file with content and ensuring it does not get stripped
    content = " Hello, World! "
    with open('test_file.txt', 'w') as f:
        f.write(content)
    
    assert get_file_content('test_file.txt', strip=False) == content
    os.remove('test_file.txt')
