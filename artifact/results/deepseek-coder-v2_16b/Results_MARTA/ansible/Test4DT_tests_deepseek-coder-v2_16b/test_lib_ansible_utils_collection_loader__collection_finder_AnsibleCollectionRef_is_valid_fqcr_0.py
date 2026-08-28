
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef



def test_invalid_collection_name():
    with pytest.raises(ValueError) as e:
        AnsibleCollectionRef('invalid-collection', 'subdir1.subdir2', 'mymodule', 'module')
    assert str(e.value) == "invalid collection name (must be of the form namespace.collection): invalid-collection"

def test_invalid_ref_type():
    with pytest.raises(ValueError) as e:
        AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'invalid_type')
    assert str(e.value) == "invalid collection ref_type: invalid_type"