
import pytest
from apimd.loader import _read

def test_read_existing_file():
    # Test reading a file that exists
    content = _read('test_file.txt')  # Assuming 'test_file.txt' is in the current directory
    assert isinstance(content, str), "Expected the content to be a string"
    with open('test_file.txt', 'r') as f:
        expected_content = f.read()