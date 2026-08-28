
# Module: ansible.utils.collection_loader._collection_finder
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys
from types import ModuleType

# Mocking the necessary modules and functions for testing
class MockModule:
    def __init__(self, **attrs):
        self.__dict__.update(attrs)

sys.modules['ansible'] = MockModule(path='mocked_path')

@pytest.fixture
def finder():
    return _AnsibleCollectionFinder(paths=['/custom/collection/path'], scan_sys_paths=True)

def test_init_with_specific_paths_and_scanning_system_paths(finder):
    assert isinstance(finder._ansible_pkg_path, str)
    assert finder._n_configured_paths == ['/custom/collection/path']
    assert finder._n_cached_collection_paths is None
    assert finder._n_cached_collection_qualified_paths is None
    assert finder._n_playbook_paths == []

def test_init_without_specifying_paths_but_scanning_system_paths(monkeypatch):
    monkeypatch.setattr(sys, 'path', ['/mocked/path1', '/mocked/path2'])
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    assert finder._ansible_pkg_path == 'mocked_path'
    assert sorted(finder._n_configured_paths) == ['/mocked/path1', '/mocked/path2']

def test_init_with_single_path_string():
    finder = _AnsibleCollectionFinder(paths='/path/to/collections')
    assert finder._n_configured_paths == ['/path/to/collections']

def test_install_method(monkeypatch, finder):
    monkeypatch.setattr(finder, '_remove', lambda: None)
    monkeypatch.setattr(sys, 'meta_path', [])
    monkeypatch.setattr(sys, 'path_hooks', [])
    from ansible.utils.collection_loader import AnsibleCollectionConfig  # Importing here to avoid undefined variable error
    
    finder._install()
    assert sys.meta_path[0] == finder
    assert sys.path_hooks[0] == finder._ansible_collection_path_hook
    assert AnsibleCollectionConfig.collection_finder == finder
