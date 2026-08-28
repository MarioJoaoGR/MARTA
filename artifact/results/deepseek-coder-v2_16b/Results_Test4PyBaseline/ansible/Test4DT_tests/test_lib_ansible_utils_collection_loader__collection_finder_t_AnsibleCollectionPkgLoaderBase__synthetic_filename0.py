
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test Case 1: Basic Initialization with Default Path List
def test_basic_initialization():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._split_name == ['ansible_collections', 'somens']
    assert loader._rpart_name[0] == 'ansible_collections'
    assert loader._rpart_name[2] == 'somens'
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'

# Test Case 2: Initialization with Custom Path List
def test_initialization_with_custom_path_list():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=['/path/to/collection'])
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._split_name == ['ansible_collections', 'somens']
    assert loader._rpart_name[0] == 'ansible_collections'
    assert loader._rpart_name[2] == 'somens'
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'
    assert '/path/to/collection' in loader._candidate_paths

# Test Case 3: Handling Invalid Fullname
def test_invalid_fullname():
    with pytest.raises(ImportError):
        _AnsibleCollectionPkgLoaderBase('invalid_fullname')

# Test Case 4: Using Default Path List and Custom Fullname
def test_default_path_list_and_custom_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.another_collection')
    assert loader._fullname == 'ansible_collections.another_collection'
    assert loader._split_name == ['ansible_collections', 'another_collection']
    assert loader._rpart_name[0] == 'ansible_collections'
    assert loader._rpart_name[2] == 'another_collection'
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'another_collection'

# Test Case 5: Handling No Path List Provided
def test_no_path_list_provided():
    with pytest.raises(ImportError):
        _AnsibleCollectionPkgLoaderBase('ansible_collections.yet_another_collection')

# Test Case 6: Synthetic Filename Method
def test_synthetic_filename_method():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._synthetic_filename('ansible_collections.somens') == '<ansible_synthetic_collection_package>'
