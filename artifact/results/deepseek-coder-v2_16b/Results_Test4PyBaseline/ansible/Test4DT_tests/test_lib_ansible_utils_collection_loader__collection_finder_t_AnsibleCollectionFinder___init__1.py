
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys

# Test initialization with default values for paths and scan_sys_paths
def test_init_default():
    finder = _AnsibleCollectionFinder()
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be of type _AnsibleCollectionFinder"
    assert not finder._n_configured_paths, "No paths should be configured by default"
    assert finder._ansible_pkg_path == os.path.dirname(sys.modules['ansible'].__file__), "Default path should be the directory of the ansible module"

# Test initialization with specific paths and enabling system path scanning
def test_init_with_specific_paths():
    finder = _AnsibleCollectionFinder(paths=['/custom/collection/path'], scan_sys_paths=True)
    assert isinstance(finder, _AnsibleCollectionFinder), "Instance should be of type _AnsibleCollectionFinder"