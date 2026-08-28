
import pytest
from ansible.parsing.dataloader import DataLoader
import os

@pytest.fixture(scope="module")
def dl():
    return DataLoader()

# Test valid input for find_vars_files method with valid path, name, and extensions
def test_valid_input(dl):
    files = dl.find_vars_files('.', 'config', ['.yaml'])
    assert isinstance(files, list), "Expected a list of file paths"
    assert len(files) > 0, "Expected at least one file to be found"
    for path in files:
        assert os.path.basename(path).startswith('config'), "File name should start with 'config'"
        assert os.path.splitext(path)[1] == '.yaml', "File extension should be .yaml"

# Test edge case for find_vars_files method with None as path and name
def test_edge_case(dl):
    files = dl.find_vars_files(None, None)
    assert isinstance(files, list), "Expected a list of file paths"
    assert len(files) == 0, "No files should be found if both path and name are None"

# Test invalid input for find_vars_files method with non-existent path and name
def test_invalid_input(dl):
    files = dl.find_vars_files('/nonexistent/path', 'noname')
    assert isinstance(files, list), "Expected a list of file paths"
    assert len(files) == 0, "No files should be found if both path and name are invalid"
