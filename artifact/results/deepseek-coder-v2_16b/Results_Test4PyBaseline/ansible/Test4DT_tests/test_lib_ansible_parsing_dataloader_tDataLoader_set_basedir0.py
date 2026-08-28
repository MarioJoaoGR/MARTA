
# Module: ansible.parsing.dataloader
# test_dataloader.py
from ansible.parsing.dataloader import DataLoader
import pytest

@pytest.fixture
def dataloader():
    return DataLoader()

def test_set_basedir(dataloader):
    basedir = '/some/directory'
    dataloader.set_basedir(basedir)
    assert dataloader._basedir == basedir

def test_load_from_file(dataloader, tmp_path):
    # Create a temporary file with some content
    content = '{"key": "value"}'
    file_path = tmp_path / 'test_file.json'
    file_path.write_text(content)
    
    # Load the content from the file
    loaded_data = dataloader.load_from_file(str(file_path))