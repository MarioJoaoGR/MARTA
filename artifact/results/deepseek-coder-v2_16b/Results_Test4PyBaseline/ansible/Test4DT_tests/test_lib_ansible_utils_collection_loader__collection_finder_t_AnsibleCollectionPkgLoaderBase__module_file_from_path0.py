
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test initialization with only the fullname provided
def test_init_with_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._split_name == ['ansible_collections', 'somens']
    assert loader._rpart_name == ('ansible_collections', '.', 'somens')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'

# Test initialization with fullname and path_list provided
def test_init_with_fullname_and_path_list():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=['/path/to/collection'])
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._split_name == ['ansible_collections', 'somens']
    assert loader._rpart_name == ('ansible_collections', '.', 'somens')
    assert loader._parent_package_name == 'ansible_collections'
    assert loader._package_to_load == 'somens'
    assert loader._candidate_paths == ['/path/to/collection']
    # The _subpackage_search_paths attribute is not tested here as it should be initialized to an empty list by default.

# Test _module_file_from_path when the submodule is a package and has no __init__.py file
def test_module_file_from_path_package_no_init():
    with pytest.raises(ImportError) as excinfo:
        _, _, _ = _AnsibleCollectionPkgLoaderBase._module_file_from_path('somens', '/some/path')
    assert str(excinfo.value) == "somens not found at /some/path"

# Test _module_file_from_path when the submodule is a module file
def test_module_file_from_path_module():
    module_path, has_code, package_path = _AnsibleCollectionPkgLoaderBase._module_file_from_path('somens', '/some/path')
    assert module_path == '/some/path/somens.py'
    assert has_code is True
    assert package_path is None
