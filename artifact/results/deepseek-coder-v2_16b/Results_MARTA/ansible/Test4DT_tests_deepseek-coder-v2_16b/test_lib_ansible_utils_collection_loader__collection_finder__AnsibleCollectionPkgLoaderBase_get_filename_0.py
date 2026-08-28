
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test Scenario 1: Valid Input
def test_valid_input():
    fullname = 'ansible_collections.somens.somodule'
    path_list = ['/path/to/collection']
    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)
    
    assert loader._fullname == fullname
    assert loader._candidate_paths == [p for p in path_list]

# Test Scenario 2: Edge Case with None or Empty List
def test_edge_case():
    # Fullname is None, path_list is empty
    loader = _AnsibleCollectionPkgLoaderBase(None)
    assert loader._fullname is None
    
    # Fullname is provided, path_list is empty
    fullname = 'ansible_collections.somens.somodule'
    path_list = []
    loader = _AnsibleCollectionPkgLoaderBase(fullname, path_list)
    assert loader._fullname == fullname
    assert loader._candidate_paths == []
    
    # Fullname is None, path_list has values
    path_list = ['/path/to/collection1', '/path/to/collection2']
    loader = _AnsibleCollectionPkgLoaderBase(None, path_list)
    assert loader._fullname is None
    assert loader._candidate_paths == [p for p in path_list]

# Test Scenario 3: Invalid Input Raises ValueError
def test_invalid_input():
    fullname = 'invalid.collection'
    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase(fullname)
