
import pytest
from ansible.parsing.dataloader import DataLoader
import os

@pytest.fixture(scope="module")
def dataloader():
    return DataLoader()

def test_valid_load_from_file(dataloader, tmpdir_factory):
    # Create a temporary file with valid YAML content
    file_path = os.path.join(str(tmpdir_factory.mktemp('data')), 'test_config.yaml')
    with open(file_path, 'w') as f:
        f.write("key: value")
    
    # Load the data from the temporary file
    data = dataloader.load_from_file(file_path)
    
    # Assert that the loaded data is correct
    assert data == {'key': 'value'}

def test_invalid_load_from_file(dataloader):
    # Provide an invalid file path
    with pytest.raises(Exception):
        dataloader.load_from_file("nonexistent_file")
