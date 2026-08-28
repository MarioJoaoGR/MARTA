
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound
import os
import yaml

# Test loading data from a non-existent file

# Test loading data from a valid YAML file
def test_valid_yaml_file(tmp_path):
    # Create a temporary YAML file with some sample data
    yaml_content = """
    key: value
    """
    yaml_file_path = tmp_path / "test.yaml"
    with open(yaml_file_path, 'w') as f:
        f.write(yaml_content)
    
    dl = DataLoader()
    data_from_file = dl.load_from_file(str(yaml_file_path))
    assert data_from_file == {'key': 'value'}

# Test loading data from a valid JSON file
def test_valid_json_file(tmp_path):
    # Create a temporary JSON file with some sample data
    json_content = """
    {
        "key": "value"
    }
    """
    json_file_path = tmp_path / "test.json"
    with open(json_file_path, 'w') as f:
        f.write(json_content)
    
    dl = DataLoader()
    data_from_file = dl.load_from_file(str(json_file_path))
    assert data_from_file == {'key': 'value'}

# Test loading data from a string in YAML format
def test_load_from_yaml_string():
    yaml_data = """
    key: value
    """
    dl = DataLoader()
    data_from_yaml_string = dl.load(yaml_data)
    assert data_from_yaml_string == {'key': 'value'}

# Test loading data from a string in JSON format
def test_load_from_json_string():
    json_data = """
    {"key": "value"}
    """
    dl = DataLoader()
    data_from_json_string = dl.load(json_data)
    assert data_from_json_string == {'key': 'value'}