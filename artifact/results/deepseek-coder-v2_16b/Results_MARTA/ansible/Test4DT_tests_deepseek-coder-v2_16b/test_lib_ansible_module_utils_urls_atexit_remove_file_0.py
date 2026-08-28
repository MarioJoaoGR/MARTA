
import os
import pytest
from unittest.mock import patch

def atexit_remove_file(filename):
    if os.path.exists(filename):
        try:
            os.unlink(filename)
        except Exception:
            pass

@pytest.fixture(scope="module")
def valid_file():
    # Create a temporary file for testing
    temp_file = "temp_test_file.txt"
    with open(temp_file, 'w') as f:
        f.write("Test content")
    yield temp_file
    os.remove(temp_file)  # Clean up after the test

def test_valid_input(valid_file):
    atexit_remove_file(valid_file)
    assert os.path.exists(valid_file)

def test_none_input():
    with pytest.raises(TypeError):
        atexit_remove_file(None)

def test_invalid_input():
    invalid_file = "non_existent_file.txt"
    with pytest.raises(FileNotFoundError):
        atexit_remove_file(invalid_file)
