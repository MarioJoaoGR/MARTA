
import pytest
from ansible.parsing.dataloader import DataLoader
import os

@pytest.fixture
def dataloader():
    return DataLoader()

# Test when there are no temporary files to clean up
def test_cleanup_all_tmp_files_no_tempfiles(dataloader):
    assert not hasattr(dataloader, '_tempfiles') or len(dataloader._tempfiles) == 0
    dataloader.cleanup_all_tmp_files()  # Corrected method name to match the function definition
    assert not hasattr(dataloader, '_tempfiles') or len(dataloader._tempfiles) == 0

# Test when there are temporary files to clean up
def test_cleanup_all_tmp_files_with_tempfiles(dataloader):
    tempfile1 = '/tmp/tempfile1'
    tempfile2 = '/tmp/tempfile2'
    dataloader._tempfiles.update([tempfile1, tempfile2])
    
    assert len(dataloader._tempfiles) == 2
    dataloader.cleanup_all_tmp_files()  # Corrected method name to match the function definition