# Module: ansible.utils.collection_loader._collection_finder
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys

# Test initialization with specific paths and enabling system path scanning
def test_init_with_specific_paths():
    finder = _AnsibleCollectionFinder(paths=['/custom/collection/path'], scan_sys_paths=True)
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be of type _AnsibleCollectionFinder"
    assert '/custom/collection/path' in finder._n_configured_paths, "Specific path should be included"
    assert any('ansible_collections' in os.path.basename(p) for p in finder._n_configured_paths), "Paths should contain 'ansible_collections'"

# Test initialization without specifying paths but including system paths
def test_init_without_specifying_paths():
    initial_sys_path = sys.path[:]  # Store the initial system path for comparison later
    finder = _AnsibleCollectionFinder(scan_sys_paths=True)
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be of type _AnsibleCollectionFinder"
    assert any('ansible_collections' in os.path.basename(p) for p in finder._n_configured_paths), "System paths should contain 'ansible_collections'"
    # Ensure the system path is not modified by this operation
    assert initial_sys_path == sys.path, "The system path should not be altered"

# Test initialization with invalid type for paths argument
def test_init_with_invalid_type_for_paths():
    with pytest.raises(TypeError):
        _AnsibleCollectionFinder(paths=123)  # Passing an integer instead of a list

# Test initialization without specifying paths and not including system paths
def test_init_without_specifying_and_not_including_system_paths():
    finder = _AnsibleCollectionFinder(scan_sys_paths=False)
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be of type _AnsibleCollectionFinder"
    assert not finder._n_configured_paths, "No paths should be configured if scan_sys_paths is False"
