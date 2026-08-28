
# Module: ansible.utils.collection_loader._collection_finder
# test_collection_loader.py
from unittest import mock
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionRootPkgLoader

@pytest.fixture
def valid_instance():
    instance = _AnsibleCollectionRootPkgLoader(fullname='ansible_collections.somens')
    instance._split_name = ['ansible_collections', 'somens']
    return instance

@pytest.fixture
def invalid_instance():
    instance = _AnsibleCollectionRootPkgLoader(fullname='ansible_collections.nested.package')
    instance._split_name = ['ansible_collections', 'nested', 'package']
    return instance

def test_valid_validate_args(valid_instance):
    with pytest.raises(ImportError) as excinfo:
        valid_instance._validate_args()
    assert str(excinfo.value) == 'this loader can only load the ansible_collections toplevel package, not ansible_collections.somens'

def test_invalid_validate_args(invalid_instance):
    with pytest.raises(ImportError) as excinfo:
        invalid_instance._validate_args()
    assert str(excinfo.value) == 'this loader can only load the ansible_collections toplevel package, not ansible_collections.nested.package'
