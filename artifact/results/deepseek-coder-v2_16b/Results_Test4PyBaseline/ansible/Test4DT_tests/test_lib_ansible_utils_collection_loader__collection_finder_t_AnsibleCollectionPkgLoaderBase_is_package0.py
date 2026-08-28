
# Module: ansible.utils.collection_loader._collection_finder
# test_collection_loader.py
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

def test_initialization_with_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._package_to_load == 'somens'

def test_initialization_with_fullname_and_path_list():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens', path_list=['/path/to/collection'])
    assert loader._fullname == 'ansible_collections.somens'
    assert loader._package_to_load == 'somens'
    assert '/path/to/collection' in loader._candidate_paths

def test_is_package_method():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    assert loader.is_package('ansible_collections.somens') is True

def test_is_package_method_with_incorrect_fullname():
    loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens')
    try:
        loader.is_package('someother.namespace.module')
    except ValueError as e:
        assert str(e) == 'this loader cannot answer is_package for someother.namespace.module, only ansible_collections.somens'
