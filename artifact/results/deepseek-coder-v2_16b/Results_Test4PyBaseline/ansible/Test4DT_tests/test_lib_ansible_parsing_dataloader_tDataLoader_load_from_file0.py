
# Module: ansible.parsing.dataloader
import pytest
from ansible.parsing.dataloader import DataLoader
import os
import yaml
import json
import copy

# Initialize the DataLoader instance
@pytest.fixture
def dataloader():
    return DataLoader()

# Test loading JSON from a file with caching enabled
def test_load_from_file_json_with_cache(dataloader, tmpdir):
    # Create a temporary JSON file with some content
    json_file = tmpdir.join('test_json.json')
    json_file.write(json.dumps({'key': 'value'}))
    
    data = dataloader.load_from_file(str(json_file), cache=True, json_only=False)
    assert isinstance(data, dict), "Expected JSON data to be a dictionary"

# Test loading JSON from a file without caching
def test_load_from_file_json_without_cache(dataloader, tmpdir):
    # Create a temporary JSON file with some content
    json_file = tmpdir.join('test_json.json')
    json_file.write(json.dumps({'key': 'value'}))
    
    first_call = dataloader.load_from_file(str(json_file), cache=False, json_only=True)
    second_call = dataloader.load_from_file(str(json_file), cache=False, json_only=True)
    assert first_call == second_call, "Expected the same result for multiple calls without caching"

# Test loading YAML from a file with caching enabled
def test_load_from_file_yaml_with_cache(dataloader, tmpdir):
    # Create a temporary YAML file with some content
    yaml_file = tmpdir.join('test_yaml.yaml')
    yaml_file.write(yaml.dump({'key': 'value'}))
    
    data = dataloader.load_from_file(str(yaml_file), cache=True, json_only=False)
    assert isinstance(data, dict), "Expected YAML data to be a dictionary"

# Test loading YAML from a file without caching
def test_load_from_file_yaml_without_cache(dataloader, tmpdir):
    # Create a temporary YAML file with some content
    yaml_file = tmpdir.join('test_yaml.yaml')
    yaml_file.write(yaml.dump({'key': 'value'}))
    
    first_call = dataloader.load_from_file(str(yaml_file), cache=False, json_only=False)
    second_call = dataloader.load_from_file(str(yaml_file), cache=False, json_only=False)