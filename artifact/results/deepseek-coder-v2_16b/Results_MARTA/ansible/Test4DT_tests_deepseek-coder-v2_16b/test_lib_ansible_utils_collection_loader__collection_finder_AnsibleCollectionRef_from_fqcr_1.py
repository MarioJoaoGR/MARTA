
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef


def test_invalid_collection_name():
    with pytest.raises(ValueError):
        # Invalid collection name should raise ValueError
        AnsibleCollectionRef('invalid-namespace.sample', 'subdir1.subdir2', 'mymodule', 'module')

def test_invalid_ref_type():
    with pytest.raises(ValueError):
        # Invalid ref_type should raise ValueError
        AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'invalid_type')

def test_invalid_subdirs():
    with pytest.raises(ValueError):
        # Invalid subdirs should raise ValueError
        AnsibleCollectionRef('ansible.sample', 'invalid-subdir', 'mymodule', 'module')


def test_from_fqcr_invalid():
    with pytest.raises(ValueError):
        # Invalid FQCR should raise ValueError
        AnsibleCollectionRef.from_fqcr('invalid.reference', 'module')