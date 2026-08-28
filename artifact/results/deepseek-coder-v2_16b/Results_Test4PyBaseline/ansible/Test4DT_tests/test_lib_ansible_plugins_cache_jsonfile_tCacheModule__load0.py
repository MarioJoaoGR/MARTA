
# Module: ansible.plugins.cache.jsonfile
import pytest
from ansible.plugins.cache.jsonfile import CacheModule
import os
import json
import codecs

# Fixture to create a temporary JSON file for testing
@pytest.fixture
def temp_json_file(tmpdir):
    data = {'key': 'value'}
    file_path = tmpdir / 'test.json'
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return str(file_path)

def test_load_with_absolute_path():
    cache_module = CacheModule()
    filepath = '/tmp/test.json'
    with open(filepath, 'w') as f:
        json.dump({'key': 'value'}, f)
    result = cache_module._load(filepath)
    assert isinstance(result, dict), "Expected a dictionary but got {}".format(type(result))
    os.remove(filepath)

def test_load_with_relative_path():
    cache_module = CacheModule()
    with open('test.json', 'w') as f:
        json.dump({'key': 'value'}, f)
    result = cache_module._load('test.json')
    assert isinstance(result, dict), "Expected a dictionary but got {}".format(type(result))
    os.remove('test.json')

def test_load_with_temp_file(temp_json_file):
    cache_module = CacheModule()
    result = cache_module._load(temp_json_file)
    assert isinstance(result, dict), "Expected a dictionary but got {}".format(type(result))

def test_load_invalid_json():
    cache_module = CacheModule()
    with open('invalid.json', 'w') as f:
        f.write('{invalid json}')
    with pytest.raises(json.JSONDecodeError):
        cache_module._load('invalid.json')
    os.remove('invalid.json')

def test_load_non_existent_file():
    cache_module = CacheModule()
    with pytest.raises(FileNotFoundError):
        cache_module._load('nonexistent.json')
