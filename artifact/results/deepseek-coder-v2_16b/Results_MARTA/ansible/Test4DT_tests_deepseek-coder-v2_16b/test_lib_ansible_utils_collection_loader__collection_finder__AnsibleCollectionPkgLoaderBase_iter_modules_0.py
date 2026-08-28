
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test Scenario 1: Valid Input
def test_valid_input():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somodule', ['/path/to/collection'])
    assert loader._fullname == 'ansible_collections.somens.somodule'
    assert loader._candidate_paths == ['/path/to/collection']

# Test Scenario 2: Edge Case - None Input or Empty Path List
def test_edge_case():
    with pytest.raises(ImportError):
        loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', None)

# Test Scenario 3: Invalid Input - Should Raise ImportError
def test_invalid_input():
    with pytest.raises(ImportError):
        loader = _AnsibleCollectionPkgLoaderBase('invalid.fullname')
