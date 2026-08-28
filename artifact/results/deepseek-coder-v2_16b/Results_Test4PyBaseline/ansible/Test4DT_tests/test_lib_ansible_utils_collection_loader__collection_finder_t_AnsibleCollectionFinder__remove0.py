
# Module: ansible.utils.collection_loader._collection_finder
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys
from types import ModuleType

# Mocking the necessary modules and functions for testing
class MockModule:
    def __init__(self, name):
        self.name = name

sys.modules['ansible'] = MockModule('ansible')

def test_initialization_with_specific_paths():
    finder = _AnsibleCollectionFinder(paths=['/custom/collection/path'], scan_sys_paths=True)
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be an instance of _AnsibleCollectionFinder"
    assert '/custom/collection/path' in finder._n_configured_paths, "Configured paths should include the specified path"

def test_initialization_without_specifying_paths():
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be an instance of _AnsibleCollectionFinder"
    assert len(finder._n_configured_paths) > 0, "Configured paths should include system paths if scan_sys_paths is True"

def test_initialization_with_single_string_path():
    finder = _AnsibleCollectionFinder(paths='/path/to/collections')
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be an instance of _AnsibleCollectionFinder"
    assert '/path/to/collections' in finder._n_configured_paths, "Configured paths should include the specified path as a single-element list"

def test_remove_method():
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    original_length = len(sys.meta_path)
    finder._remove()
    assert len(sys.meta_path) == original_length - 1, "The finder should be removed from sys.meta_path"
    assert not hasattr(finder, 'AnsibleCollectionConfig'), "The collection finder should be reset in AnsibleCollectionConfig"
