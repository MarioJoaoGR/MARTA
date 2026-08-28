# Module: ansible.galaxy.api
import os
import stat
import json
from ansible.galaxy.api import _load_cache

def test_load_cache_creates_new_file():
    b_cache_path = 'test_cache_file'
    result = _load_cache(b_cache_path)
    assert os.path.isfile(b_cache_path), "Cache file should be created"
    with open(b_cache_path, mode='r') as fd:
        cache = json.load(fd)
    assert isinstance(cache, dict), "Newly created cache should be a dictionary"
    assert 'version' in cache, "Newly created cache should have a version key"
    os.remove(b_cache_path)

def test_load_cache_with_existing_file():
    b_cache_path = 'test_cache_file'
    with open(b_cache_path, mode='w') as fd:
        json.dump({'version': 1}, fd)
    result = _load_cache(b_cache_path)
    assert isinstance(result, dict), "Existing cache should be loaded as a dictionary"
    os.remove(b_cache_path)

def test_load_cache_with_invalid_version():
    b_cache_path = 'test_cache_file'
    with open(b_cache_path, mode='w') as fd:
        json.dump({'version': 0}, fd)
    result = _load_cache(b_cache_path)
    assert isinstance(result, dict), "Cache should be re-created if version is invalid"
    with open(b_cache_path, mode='r') as fd:
        cache = json.load(fd)
    assert cache['version'] == 1, "Re-created cache should have the correct version"
    os.remove(b_cache_path)

def test_load_cache_with_world_writable_file():
    b_cache_path = 'test_cache_file'
    with open(b_cache_path, mode='w') as fd:
        json.dump({'version': 1}, fd)
    os.chmod(b_cache_path, stat.S_IWOTH)
    result = _load_cache(b_cache_path)
    assert result is None, "Cache should be ignored if the file has world writable access"
    os.remove(b_cache_path)

def test_load_cache_with_non_existent_file():
    b_cache_path = 'non_existent_cache_file'
    result = _load_cache(b_cache_path)
    assert isinstance(result, dict), "Non-existent cache should be created"
    with open(b_cache_path, mode='r') as fd:
        cache = json.load(fd)
    assert 'version' in cache, "Created cache file should have a version key"
    os.remove(b_cache_path)
