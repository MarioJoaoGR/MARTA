
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef



def test_invalid_collection_name():
    with patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef', autospec=True):
        with pytest.raises(ValueError) as excinfo:
            acr = AnsibleCollectionRef('invalid-collection', 'subdir1.subdir2', 'mymodule', 'module')
        assert str(excinfo.value) == "invalid collection name (must be of the form namespace.collection): invalid-collection"

def test_invalid_ref_type():
    with patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef', autospec=True):
        with pytest.raises(ValueError) as excinfo:
            acr = AnsibleCollectionRef('ansible.sample', 'subdir1.subdir2', 'mymodule', 'invalid_type')
        assert str(excinfo.value) == "invalid collection ref_type: invalid_type"