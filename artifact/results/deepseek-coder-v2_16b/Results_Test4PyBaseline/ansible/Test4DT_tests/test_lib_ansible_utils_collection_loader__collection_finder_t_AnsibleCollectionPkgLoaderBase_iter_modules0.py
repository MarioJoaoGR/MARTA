
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test initialization with full name only
def test_init_with_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._package_to_load == 'somens'

# Test initialization with full name and path list
def test_init_with_fullname_and_pathlist():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=['/path/to/collection'])
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._package_to_load == 'somens'
    assert '/path/to/collection' in loader._candidate_paths

# Test iterating modules with prefix
def test_iter_modules():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.module', ['/path/to/collection'])
    results = list(loader.iter_modules(''))
    assert len(results) > 0, "Expected at least one module or package to be found"
    for result in results:
        assert isinstance(result, tuple), "Each result should be a tuple"
        assert len(result) == 2, "Each tuple should contain two elements"

# Test initialization with invalid full name
def test_init_with_invalid_fullname():
    try:
        loader = _AnsibleCollectionPkgLoaderBase('invalid_namespace.somens')
    except ImportError as e:
        assert str(e) == 'this loader can only load collection packages, not invalid_namespace.somens'

# Test initialization without path list provided
def test_init_without_pathlist():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert len(loader._candidate_paths) == 0

if __name__ == '__main__':
    pytest.main()
