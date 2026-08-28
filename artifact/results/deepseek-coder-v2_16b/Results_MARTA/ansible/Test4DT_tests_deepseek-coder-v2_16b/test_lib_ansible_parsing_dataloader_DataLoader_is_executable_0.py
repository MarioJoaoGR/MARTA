
import pytest
from ansible.parsing.dataloader import DataLoader
import os

@pytest.fixture(scope="module")
def dl():
    return DataLoader()

# Test loading data from a valid string input
def test_valid_case_load_from_string(dl):
    data_from_string = dl.load('{"key": "value"}')
    assert isinstance(data_from_string, dict)
    assert data_from_string == {"key": "value"}

# Test loading data from a valid file input
def test_valid_case_load_from_file(dl):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'test_config.yaml')
    with open(file_path, 'w') as f:
        f.write('key: value')
    data_from_file = dl.load_from_file(file_path)
    assert isinstance(data_from_file, dict)
    assert data_from_file == {"key": "value"}
    os.remove(file_path)

# Test handling invalid input by raising an error
def test_error_case_invalid_input(dl):
    with pytest.raises(Exception):
        dl.load(None)
