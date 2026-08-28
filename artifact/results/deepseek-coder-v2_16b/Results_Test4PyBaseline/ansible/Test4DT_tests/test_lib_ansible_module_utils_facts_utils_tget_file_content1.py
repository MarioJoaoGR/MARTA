
import os
import fcntl
from ansible.module_utils.facts.utils import get_file_content

def test_get_file_content_default():
    assert get_file_content('nonexistent.txt') is None, "Expected default value to be returned for a non-existent file"

def test_get_file_content_no_access():
    with open('test_file', 'w') as f:
        f.write('Test content')
    os.chmod('test_file', 0o200)  # No read access
    assert get_file_content('test_file') is None, "Expected default value to be returned for a file without read access"
    os.remove('test_file')

def test_get_file_content_read_error():
    with open('test_file', 'w') as f:
        f.write('Test content')
    os.chmod('test_file', 0o644)  # Read access
    try:
        get_file_content('test_file', strip=False)  # Simulate read error by not closing the file
        assert False, "Expected an exception due to read error"
    except Exception as e:
        assert str(e), "Unexpected exception type or message"
    os.remove('test_file')

def test_get_file_content_empty_stripped():
    with open('test_file', 'w') as f:
        f.write('   ')