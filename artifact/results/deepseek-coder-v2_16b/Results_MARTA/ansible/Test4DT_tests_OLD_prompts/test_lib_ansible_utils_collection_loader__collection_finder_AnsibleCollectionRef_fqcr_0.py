
import pytest
from unittest.mock import patch
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef, to_text, to_native



def test_invalid_collection_name():
    with pytest.raises(ValueError) as e:
        collection_ref = AnsibleCollectionRef('invalid_namespace', None, 'mymodule', 'module')
    assert str(e.value) == 'invalid collection name (must be of the form namespace.collection): invalid_namespace'

def test_invalid_ref_type():
    with pytest.raises(ValueError) as e:
        collection_ref = AnsibleCollectionRef('ansible.sample', None, 'mymodule', 'invalid_type')
    assert str(e.value) == 'invalid collection ref_type: invalid_type'