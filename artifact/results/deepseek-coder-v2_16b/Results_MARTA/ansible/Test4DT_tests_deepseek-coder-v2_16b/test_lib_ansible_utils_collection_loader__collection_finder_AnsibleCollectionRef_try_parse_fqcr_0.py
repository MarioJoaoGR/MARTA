
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
import re


def test_invalid_collection_name():
    with pytest.raises(ValueError):
        collection_name = 'invalid-namespace.sample'
        subdirs = None
        resource = 'mymodule'
        ref_type = 'module'
        
        AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

def test_invalid_ref_type():
    with pytest.raises(ValueError):
        collection_name = 'ansible.sample'
        subdirs = None
        resource = 'mymodule'
        ref_type = 'invalid_type'
        
        AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)


def test_invalid_subdirs():
    with pytest.raises(ValueError):
        collection_name = 'ansible.sample'
        subdirs = 'invalid-subdir'
        resource = 'mymodule'
        ref_type = 'module'
        
        AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)