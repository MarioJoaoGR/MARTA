
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys

# Test initialization with default parameters
def test_valid_input_default_init():
    finder = _AnsibleCollectionFinder()
    assert hasattr(finder, '_n_configured_paths')
    assert finder._n_configured_paths == []
    assert not hasattr(finder, 'paths')
    assert not hasattr(finder, 'scan_sys_paths')

# Test initialization with provided specific paths and enabled system path scanning
def test_valid_input_specific_paths():
    paths = ['/path/to/collection1', '/path/to/collection2']
    finder = _AnsibleCollectionFinder(paths=paths, scan_sys_paths=True)
    assert hasattr(finder, '_n_configured_paths')
    assert finder._n_configured_paths == paths
    assert finder.scan_sys_paths is True

# Test initialization with None for paths, should default to empty list
def test_invalid_input_none_paths():
    finder = _AnsibleCollectionFinder(paths=None, scan_sys_paths=True)
    assert hasattr(finder, '_n_configured_paths')
    assert finder._n_configured_paths == []
    assert not hasattr(finder, 'paths')
    assert finder.scan_sys_paths is True
