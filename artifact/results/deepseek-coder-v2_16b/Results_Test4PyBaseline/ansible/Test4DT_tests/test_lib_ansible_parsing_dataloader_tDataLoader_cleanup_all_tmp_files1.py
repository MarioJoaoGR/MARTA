
# Module: ansible.parsing.dataloader
import pytest
from ansible.parsing.dataloader import DataLoader
import os

@pytest.fixture
def dataloader():
    return DataLoader()

def test_cleanup_all_tmp_files_no_tempfiles(dataloader):
    # Test when there are no temporary files to clean up
    assert not hasattr(dataloader, '_tempfiles') or len(dataloader._tempfiles) == 0
    dataloader.cleanup_all_tmp_files()
    assert not hasattr(dataloader, '_tempfiles') or len(dataloader._tempfiles) == 0

def test_cleanup_all_tmp_files_with_tempfiles(dataloader):
    # Test when there are temporary files to clean up
    tempfile1 = '/tmp/tempfile1'
    tempfile2 = '/tmp/tempfile2'
    dataloader._tempfiles.update([tempfile1, tempfile2])
    