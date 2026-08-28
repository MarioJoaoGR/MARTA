
import pytest
from pathlib import Path
from flutils.pathutils import exists_as
import os

# Helper function to create temporary directory and file for testing
def setup_temp_directory_and_file():
    temp_dir = Path(os.path.expanduser('~/tmp'))
    temp_dir.mkdir(exist_ok=True)
    temp_file = temp_dir / 'example.txt'
    temp_file.touch()
    return str(temp_dir), str(temp_file)

def setup_invalid_path():
    invalid_path = os.path.expanduser('~/nonexistent')
    return invalid_path

# Test for a valid directory
def test_valid_directory():
    temp_dir, _ = setup_temp_directory_and_file()
    assert exists_as(temp_dir) == 'directory'

# Test for a valid file
def test_valid_file():
    _, temp_file = setup_temp_directory_and_file()
    assert exists_as(temp_file) == 'file'

# Test for an invalid path
def test_invalid_path():
    invalid_path = setup_invalid_path()
    assert exists_as(invalid_path) == ''
