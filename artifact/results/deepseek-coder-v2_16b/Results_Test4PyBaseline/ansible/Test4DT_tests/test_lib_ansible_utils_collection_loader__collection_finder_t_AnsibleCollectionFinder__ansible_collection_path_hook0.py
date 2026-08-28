
# Module: ansible.utils.collection_loader._collection_finder
# test_collection_finder.py
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder, _AnsiblePathHookFinder
import os
import sys

def test_init_with_specific_paths():
    finder = _AnsibleCollectionFinder(paths=['/custom/collection/path'], scan_sys_paths=True)
    assert hasattr(finder, '_n_configured_paths')
    assert '/custom/collection/path' in finder._n_configured_paths

def test_init_without_specific_paths():
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    assert hasattr(finder, '_n_configured_paths')
    assert len(finder._n_configured_paths) > 0

def test_init_with_multiple_paths():
    finder = _AnsibleCollectionFinder(paths=['/path1', '/path2'], scan_sys_paths=True)
    assert hasattr(finder, '_n_configured_paths')
    assert '/path1' in finder._n_configured_paths
    assert '/path2' in finder._n_configured_paths

def test_init_without_system_path_scanning():
    finder = _AnsibleCollectionFinder(paths=['/path1'], scan_sys_paths=False)
    assert hasattr(finder, '_n_configured_paths')
    assert '/path1' in finder._n_configured_paths
    assert len(finder._n_configured_paths) == 1

def test_ansible_collection_path_hook():
    # Assuming _AnsibleCollectionFinder has a method to set paths or cache them for testing purposes
    finder = _AnsibleCollectionFinder()
    # Mocking the path setup for testing
    finder._n_collection_paths = ['/mocked/path']
    hook = finder._ansible_collection_path_hook('/mocked/path/to/interesting')
    assert isinstance(hook, _AnsiblePathHookFinder)
