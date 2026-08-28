
import pytest
import os
from apimd.loader import _read

# Scenario 1: Test reading a valid file
def test_valid_file_read():
    # Ensure 'script.py' exists in the current directory with some content
    expected_content = "print('Hello, World!')"
    with open('script.py', 'w') as f:
        f.write(expected_content)
    
    assert _read('script.py') == expected_content
    os.remove('script.py')  # Clean up after the test

# Scenario 2: Test handling None input
def test_none_input():
    with pytest.raises(TypeError):
        _read(None)

# Scenario 3: Test reading a non-existent file
def test_non_existent_file():
    with pytest.raises(FileNotFoundError):
        _read('nonexistent.txt')
