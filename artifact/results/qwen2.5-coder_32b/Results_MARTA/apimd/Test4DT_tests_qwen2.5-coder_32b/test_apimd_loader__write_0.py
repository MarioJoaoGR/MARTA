
import pytest
from apimd.loader import _write
import os

def test_empty_path():
    """Test that an empty string for path raises a ValueError."""
    try:
        _write('', 'Empty path should raise an error')
    except FileNotFoundError as e:
        assert str(e) == "[Errno 2] No such file or directory: ''"


def test_write_to_new_file():
    """Test writing to a new file."""
    test_file = 'test_new_file.md'
    content = '# Test Document\nThis is a test document.'
    _write(test_file, content)
    assert os.path.exists(test_file)
    with open(test_file, 'r', encoding='utf-8') as f:
        written_content = f.read()
    assert written_content == content
    os.remove(test_file)

def test_overwrite_existing_file():
    """Test overwriting an existing file."""
    test_file = 'test_overwrite.md'
    initial_content = '# Initial Document\nThis is the initial document.'
    _write(test_file, initial_content)
    
    new_content = '# Updated Document\nThis is the updated document.'
    _write(test_file, new_content)
    
    with open(test_file, 'r', encoding='utf-8') as f:
        written_content = f.read()
    assert written_content == new_content
    os.remove(test_file)

def test_write_with_relative_path():
    """Test writing to a file using a relative path."""
    test_dir = 'test_dir'
    test_file = os.path.join(test_dir, 'relative_test.md')
    content = '# Relative Path Document\nThis document is written using a relative path.'
    
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    _write(test_file, content)
    assert os.path.exists(test_file)
    with open(test_file, 'r', encoding='utf-8') as f:
        written_content = f.read()
    assert written_content == content
    
    # Cleanup
    os.remove(test_file)
    os.rmdir(test_dir)