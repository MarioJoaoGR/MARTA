
import os
import json
import stat
from ansible.galaxy.api import _load_cache
import pytest

def test_valid_cache_load():
    # Create a valid cache file for testing
    with open('/tmp/valid_cachefile', 'w') as f:
        json.dump({'version': 1}, f)
    
    result = _load_cache('/tmp/valid_cachefile')
    assert isinstance(result, dict), "Expected a dictionary but got something else"
    assert result['version'] == 1, "Expected version 1 but got a different version"
    os.remove('/tmp/valid_cachefile')

def test_missing_cache_file():
    # Test when the cache file does not exist
    with pytest.raises(FileNotFoundError):
        _load_cache('/non/existent/path')

def test_invalid_cache_content():
    # Create an invalid cache file for testing
    with open('/tmp/invalid_cachefile', 'w') as f:
        json.dump({'wrong': 'data'}, f)
    
    result = _load_cache('/tmp/invalid_cachefile')
    assert isinstance(result, dict), "Expected a dictionary but got something else"
    assert result['version'] == 1, "Expected version 1 but got a different version"
    os.remove('/tmp/invalid_cachefile')
