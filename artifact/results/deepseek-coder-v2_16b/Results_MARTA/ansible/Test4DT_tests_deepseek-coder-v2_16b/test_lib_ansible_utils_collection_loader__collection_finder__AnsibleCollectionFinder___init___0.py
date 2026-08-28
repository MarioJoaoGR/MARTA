
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys

@pytest.fixture(scope="module")
def finder():
    return _AnsibleCollectionFinder()

def test__init__default_initialization(finder):
    assert hasattr(finder, '_ansible_pkg_path')
    assert hasattr(finder, '_n_configured_paths')
    assert hasattr(finder, '_n_cached_collection_paths')
    assert hasattr(finder, '_n_cached_collection_qualified_paths')
    assert hasattr(finder, '_n_playbook_paths')


