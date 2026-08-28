
import pytest
from ansible.parsing.dataloader import DataLoader
import os
import tempfile

# Test loading valid YAML file from disk
def test_valid_input_load_from_file():
    dl = DataLoader()
    with open('tests/data/valid.yaml', 'r') as f:
        data = dl.load_from_file(f.name)
    assert isinstance(data, dict), "Loaded data is not a dictionary"
    assert len(data) > 0, "Loaded data is empty"

# Test handling None input in load method
def test_none_input_load():
    dl = DataLoader()
    with pytest.raises(TypeError):
        dl.load(None)

# Test loading from an invalid file path
def test_invalid_file_path_load_from_file():
    dl = DataLoader()
    with pytest.raises(FileNotFoundError):
        dl.load_from_file('nonexistent.yaml')
