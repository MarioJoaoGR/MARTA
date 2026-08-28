
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test scenarios
def test_valid_input():
    # Setup: Real instance of _AnsibleCollectionPkgLoaderBase with minimal args
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somodule')
    
    assert loader._fullname == 'ansible_collections.somens.somodule'
    assert loader._split_name == ['ansible_collections', 'somens', 'somodule']
    assert loader._rpart_name == ('ansible_collections.somens', 'somodule')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'

def test_edge_case():
    # Setup: None
    with pytest.raises(TypeError):
        _AnsibleCollectionPkgLoaderBase()

def test_invalid_input():
    # Setup: Real instance of _AnsibleCollectionPkgLoaderBase with invalid args
    with pytest.raises(ImportError):
        loader = _AnsibleCollectionPkgLoaderBase('invalid.fullname')
