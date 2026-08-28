
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
import re



def test_invalid_case():
    with pytest.raises(ValueError):
        collection_name = 'invalid-namespace'
        subdirs = 'subdir1.subdir2'
        resource = 'mymodule'
        ref_type = 'module'
        
        AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

def test_invalid_ref_type():
    with pytest.raises(ValueError):
        collection_name = 'ansible.sample'
        subdirs = 'subdir1.subdir2'
        resource = 'mymodule'
        ref_type = 'invalid_type'
        
        AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)