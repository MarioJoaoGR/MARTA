
import pytest
from ansible.parsing.dataloader import DataLoader
import os

@pytest.fixture(scope="module")
def dataloader():
    return DataLoader()


def test_invalid_file_path_load_from_file(dataloader):
    file_path = '/nonexistent/file.yaml'  # Assuming the file does not exist
    with pytest.raises(Exception) as e:
        dataloader.load_from_file(file_path)
    assert str(e.value).startswith("Unable to retrieve file contents"), f"Expected an AnsibleFileNotFound error but got {str(e.value)}"