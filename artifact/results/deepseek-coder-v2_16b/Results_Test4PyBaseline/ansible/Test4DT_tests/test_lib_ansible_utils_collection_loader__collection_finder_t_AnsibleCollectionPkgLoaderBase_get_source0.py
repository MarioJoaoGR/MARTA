
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test initialization with a valid fullname and no path list
def test_init_with_valid_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._package_to_load == 'somens'

# Test initialization with a valid fullname and path list
def test_init_with_valid_fullname_and_path_list():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=['/path/to/collection'])
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._package_to_load == 'somens'
    assert '/path/to/collection' in loader._candidate_paths

# Test initialization with an invalid fullname
def test_init_with_invalid_fullname():
    with pytest.raises(ImportError):
        _AnsibleCollectionPkgLoaderBase('invalid.fullname')

# Test initialization with an invalid path list
def test_init_with_invalid_path_list():
    with pytest.raises(ValueError):
        _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=['invalid/path'])

# Test get_source method with a valid fullname
def test_get_source_with_valid_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    source = loader.get_source('ansible_collections.somens')
    assert source is None  # Assuming get_source method returns None if the source code path is not set

# Test get_source method with an invalid fullname
def test_get_source_with_invalid_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    with pytest.raises(ValueError):
        loader.get_source('invalid.fullname')
