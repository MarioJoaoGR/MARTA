
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase
import os

# Helper function to create a temporary directory for testing
@pytest.fixture(scope="module")
def temp_dir():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmp_dir:
        yield tmp_dir

# Test initialization without path list
def test_init_without_path_list():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._split_name == ['ansible_collections', 'somens']
    assert loader._rpart_name == ('ansible_collections.', '.somens')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'

# Test initialization with path list
def test_init_with_path_list(temp_dir):
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=[temp_dir])
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._split_name == ['ansible_collections', 'somens']
    assert loader._rpart_name == ('ansible_collections.', '.somens')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'
    assert temp_dir in loader._candidate_paths

# Test getting data with valid absolute path
def test_get_data_valid_path(temp_dir):
    # Create a temporary file for testing
    temp_file_path = os.path.join(temp_dir, 'test_file.txt')
    with open(temp_file_path, 'w') as f:
        f.write('Test content')
    
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=[temp_dir])
    data = loader.get_data(f'{temp_dir}/test_file.txt')
    assert data == b'Test content'

# Test getting data with invalid absolute path
def test_get_data_invalid_path():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=[])
    with pytest.raises(ValueError):
        loader.get_data('/nonexistent/path/__init__.py')

# Test getting data without a path specified
def test_get_data_no_path():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=[])
    with pytest.raises(ValueError):
        loader.get_data(None)

# Test getting data with relative path
def test_get_data_relative_path():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=[])
    with pytest.raises(ValueError):
        loader.get_data('relative/path/__init__.py')
