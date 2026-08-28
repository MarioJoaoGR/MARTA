
# Module: ansible.parsing.dataloader
import os
from ansible.parsing.dataloader import DataLoader
import pytest

@pytest.fixture
def dataloader():
    return DataLoader()

# Test cases for find_vars_files method
def test_find_vars_files_basic(dataloader):
    found_files = dataloader.find_vars_files('.', 'config')
    assert isinstance(found_files, list), "Expected a list of file paths"
    for path in found_files:
        assert os.path.exists(str(path)), f"File {str(path)} does not exist"

def test_find_vars_files_specify_extensions(dataloader):
    found_files = dataloader.find_vars_files('.', '', ['.yaml', '.yml'])
    assert isinstance(found_files, list), "Expected a list of file paths"
    for path in found_files:
        ext = os.path.splitext(str(path))[1]
        assert ext in ['.yaml', '.yml'], f"Unexpected extension {ext} found in {str(path)}"

def test_find_vars_files_restrict_to_files(dataloader):
    found_files = dataloader.find_vars_files('.', '', ['.yaml', '.yml'], allow_dir=False)
    assert isinstance(found_files, list), "Expected a list of file paths"
    for path in found_files:
        assert not os.path.isdir(str(path)), f"{str(path)} is a directory"

def test_find_vars_files_default_extensions(dataloader):
    found_files = dataloader.find_vars_files('.', 'vars')
    assert isinstance(found_files, list), "Expected a list of file paths"
    for path in found_files:
        ext = os.path.splitext(str(path))[1]
        assert ext in ['.yaml', '.yml'] or ext == '', f"Unexpected extension {ext} found in {str(path)}"
