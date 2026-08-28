# Module: ansible.utils.collection_loader._collection_finder
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

# Test initialization with full name only
def test_init_with_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._package_to_load == 'somens'

# Test initialization with full name and custom path list
def test_init_with_fullname_and_pathlist():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=['/path/to/collection'])
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._package_to_load == 'somens'
    assert '/path/to/collection' in loader._candidate_paths

# Test handling ImportError when full name does not start with 'ansible_collections'
def test_init_with_invalid_fullname():
    try:
        _AnsibleCollectionPkgLoaderBase('not_ansible_collections.somens')
    except ImportError as e:
        assert str(e) == "ImportError: this loader can only load collection packages, not not_ansible_collections.somens"

# Test using default path list when none is provided
def test_init_with_default_pathlist():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert len(loader._candidate_paths) == 0

if __name__ == "__main__":
    pytest.main()
