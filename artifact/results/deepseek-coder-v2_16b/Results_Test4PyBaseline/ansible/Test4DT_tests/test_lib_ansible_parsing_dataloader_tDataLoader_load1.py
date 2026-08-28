
# Module: ansible.parsing.dataloader
# test_dataloader.py
from ansible.parsing.dataloader import DataLoader
import pytest

@pytest.fixture
def dataloader():
    return DataLoader()

def test_load_from_string(dataloader):
    data = '{"key": "value"}'
    result = dataloader.load(data)
    assert result == {'key': 'value'}

def test_load_from_file(dataloader, tmp_path):
    file_content = '{"key": "value"}'
    file_path = tmp_path / 'test_file.json'
    with open(file_path, 'w') as f:
        f.write(file_content)
    result = dataloader.load_from_file(str(file_path))
    assert result == {'key': 'value'}

def test_load_json_only(dataloader, tmp_path):
    file_content = '{"key": "value"}'
    file_path = tmp_path / 'test_file.json'
    with open(file_path, 'w') as f:
        f.write(file_content)
    result = dataloader.load_from_file(str(file_path), json_only=True)
    assert result == {'key': 'value'}

def test_set_vault_secrets(dataloader):
    dataloader.set_vault_secrets({'password': 'secret'})
    assert dataloader._vault.secrets == {'password': 'secret'}

def test_load_with_cache(dataloader, tmp_path):
    file_content = '{"key": "value"}'
    file_path = tmp_path / 'test_file.json'
    with open(file_path, 'w') as f:
        f.write(file_content)
    # First load should populate the cache
    dataloader.load_from_file(str(file_path))
    # Second load should use the cached result
    assert dataloader.load_from_file(str(file_path)) == {'key': 'value'}

# Additional test cases for from_yaml function
def test_from_yaml_valid_json(dataloader):
    data = '{"key": "value"}'
    result = dataloader.load(data, json_only=False)