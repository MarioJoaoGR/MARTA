
import pytest
from unittest.mock import patch
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase



def test_get_data_invalid_path():
    with patch('ansible.utils.collection_loader._collection_finder._AnsibleCollectionPkgLoaderBase.__init__', return_value=None):
        loader = _AnsibleCollectionPkgLoaderBase('ansible_collections.somens.somodule')
        data = loader.get_data('/invalid/path/to/module/__init__.py')
        assert data is None