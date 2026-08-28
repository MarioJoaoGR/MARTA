
import os
from ansible.module_utils.facts.system.distribution import _file_exists

def test_file_does_not_exist():
    path = '/nonexistent/file'
    result = _file_exists(path)
    assert not result, f"Expected False for non-existent file but got {result}"

def test_file_exists_without_allow_empty():
    with open('/tmp/testfile', 'w') as f:
        f.write('content')  # Create a non-empty file
    path = '/tmp/testfile'
    result = _file_exists(path)
    assert not result, f"Expected False for existing but non-empty file without allow_empty={result}"

def test_file_exists_with_allow_empty():
    with open('/tmp/emptestfile', 'w') as f:
        pass  # Create an empty file
    path = '/tmp/emptestfile'
    result = _file_exists(path, allow_empty=True)
    assert result, f"Expected True for existing but empty file with allow_empty={result}"

def test_file_exists_and_not_allow_empty():
    path = '/tmp/testfile'
    with open(path, 'w') as f:
        f.write('content')  # Create a non-empty file
    result = _file_exists(path)
    assert not result, f"Expected False for existing but non-empty file without allow_empty={result}"
