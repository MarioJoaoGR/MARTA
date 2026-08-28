# Module: ansible.parsing.dataloader
# test_dataloader.py
import pytest
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_get_basedir(dataloader):
    assert dataloader.get_basedir() == '.'
