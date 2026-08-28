
import pytest
from ansible.parsing.dataloader import DataLoader
import os

@pytest.fixture(scope="module")
def dl():
    return DataLoader()

# Test loading from a valid file path
def test_valid_input_load_from_file(dl):
    # Load data from a valid file path
    data = dl.load_from_file('tests/data/valid_config.yaml')
    assert isinstance(data, dict), "Loaded data should be a dictionary"
    assert 'key' in data, "The loaded data should contain the key 'key'"
    assert data['key'] == 'value', "The value of 'key' should be 'value'"

# Test checking if an invalid path is considered as a file
def test_invalid_path_is_file(dl):
    with pytest.raises(IOError) as excinfo:
        dl.load_from_file('non_existent_file')
    assert "No such file or directory" in str(excinfo.value), "Expected an IOError for a non-existent file"

# Test error handling with an invalid input type for load method
def test_error_handling_invalid_input(dl):
    with pytest.raises(TypeError) as excinfo:
        dl.load(12345)
    assert "Expected str, bytes or os.PathLike object" in str(excinfo.value), "Expected a TypeError for invalid input type"
