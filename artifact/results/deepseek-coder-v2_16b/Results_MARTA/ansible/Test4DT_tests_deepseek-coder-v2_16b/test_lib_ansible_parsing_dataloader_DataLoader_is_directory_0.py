
import os
import pytest
from ansible.parsing.dataloader import DataLoader

@pytest.fixture(scope="module")
def dl():
    return DataLoader()

# Test for a valid directory path returning True
def test_valid_is_directory(dl):
    dl._basedir = '/'
    path = '/tmp'
    assert dl.is_directory(path) == os.path.isdir(path), f"Expected is_directory('/tmp') to be True, but got {dl.is_directory(path)}"

# Test for an invalid directory path returning False
def test_invalid_is_directory(dl):
    dl._basedir = '/'
    path = '/nonexistent'
    assert dl.is_directory(path) == os.path.isdir(path), f"Expected is_directory('/nonexistent') to be False, but got {dl.is_directory(path)}"

# Test for a file path returning False
def test_non_directory_is_directory(dl):
    dl._basedir = '/'
    path = '/etc/passwd'
    assert not dl.is_directory(path), f"Expected is_directory('/etc/passwd') to be False, but got {dl.is_directory(path)}"
