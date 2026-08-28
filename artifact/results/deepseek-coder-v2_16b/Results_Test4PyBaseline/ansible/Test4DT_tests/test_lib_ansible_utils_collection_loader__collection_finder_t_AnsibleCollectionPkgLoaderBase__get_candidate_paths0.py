
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase
import os

# Test initialization with only fullname
def test_init_with_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._split_name == ['ansible_collections', 'somens']
    assert loader._rpart_name == ('ansible_collections', '.', 'somens')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'

# Test initialization with fullname and path list
def test_init_with_fullname_and_pathlist():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=['/path/to/collection'])
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._split_name == ['ansible_collections', 'somens']
    assert loader._rpart_name == ('ansible_collections', '.', 'somens')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'
    assert loader._candidate_paths == ['/path/to/collection/somens']

# Test default behavior without path list
def test_init_without_pathlist():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._split_name == ['ansible_collections', 'somens']
    assert loader._rpart_name == ('ansible_collections', '.', 'somens')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'
    assert loader._candidate_paths == []

# Test _get_candidate_paths method
def test_get_candidate_paths():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=['/path/to/collection'])
    candidate_paths = loader._get_candidate_paths(['/path/to/collection'])
    assert candidate_paths == ['/path/to/collection/somens']
