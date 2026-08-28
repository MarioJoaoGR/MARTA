# Module: ansible.plugins.cache.jsonfile
import pytest
from ansible.plugins.cache.jsonfile import CacheModule
import json
import codecs  # Required for Python 3 compatibility
from ansible.plugins.jsonencoder import AnsibleJSONEncoder
from ansible.plugins.jsondecoder import AnsibleJSONDecoder

# Fixture to create an instance of CacheModule for testing
@pytest.fixture
def cache_module():
    return CacheModule()

# Test case for _dump method
def test_cache_module__dump(tmpdir, cache_module):
    value = {'key': 'value', 'number': 123}
    filepath = tmpdir.join("test_file.json")
    
    # Call the _dump method
    cache_module._dump(value, str(filepath))
    
    # Read and parse the file to check if it contains the expected data
    with codecs.open(str(filepath), 'r', encoding='utf-8') as f:
        content = json.load(f, cls=AnsibleJSONDecoder)
    
    assert content == value

# Test case for _load method
def test_cache_module__load(tmpdir, cache_module):
    value = {'key': 'value', 'number': 123}
    filepath = tmpdir.join("test_file.json")
    
    # Write the dictionary to the file
    with codecs.open(str(filepath), 'w', encoding='utf-8') as f:
        json.dump(value, f, cls=AnsibleJSONEncoder, sort_keys=True, indent=4)
    
    # Call the _load method and check if it returns the expected dictionary
    loaded_data = cache_module._load(str(filepath))
    
    assert loaded_data == value
