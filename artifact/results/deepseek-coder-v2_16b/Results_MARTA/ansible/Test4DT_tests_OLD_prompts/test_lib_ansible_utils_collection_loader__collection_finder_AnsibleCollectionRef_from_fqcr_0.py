
import pytest
from unittest.mock import patch, MagicMock
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef


def test_invalid_collection_name():
    with pytest.raises(ValueError):
        with patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef') as mock_class:
            mock_instance = MagicMock()
            mock_class.return_value = mock_instance

            collection_name = 'invalid-collection'
            subdirs = None
            resource = 'mymodule'
            ref_type = 'module'

            AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

def test_invalid_ref_type():
    with pytest.raises(ValueError):
        with patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef') as mock_class:
            mock_instance = MagicMock()
            mock_class.return_value = mock_instance

            collection_name = 'ansible.sample'
            subdirs = None
            resource = 'mymodule'
            ref_type = 'invalid_type'

            AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)

def test_invalid_subdirs():
    with pytest.raises(ValueError):
        with patch('ansible.utils.collection_loader._collection_finder.AnsibleCollectionRef') as mock_class:
            mock_instance = MagicMock()
            mock_class.return_value = mock_instance

            collection_name = 'ansible.sample'
            subdirs = 'invalid-subdirs'
            resource = 'mymodule'
            ref_type = 'module'

            AnsibleCollectionRef(collection_name, subdirs, resource, ref_type)