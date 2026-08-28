
import pytest
from unittest.mock import patch
from ansible.utils.collection_loader._collection_finder import _get_collection_metadata, _nested_dict_get
from ansible.utils.collection_loader._collection_finder import _AnsibleInternalRedirectLoader

def test_valid_module_import():
    with patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata', return_value={'import_redirection': {'ansible.network.network_cli': {'redirect': 'ansible.network.network_cli'}}}):
        try:
            loader = _AnsibleInternalRedirectLoader('ansible.network.network_cli', [])
            assert loader._redirect == 'ansible.network.network_cli'
        except ImportError as e:
            pytest.fail(f"Import error: {e}")

def test_invalid_package_fullname():
    with patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata', return_value={}):
        with pytest.raises(ImportError) as e:
            loader = _AnsibleInternalRedirectLoader('notansible.network.network_cli', [])
            assert 'not interested' in str(e.value)

def test_missing_module_in_metadata():
    with patch('ansible.utils.collection_loader._collection_finder._get_collection_metadata', return_value={}):
        with pytest.raises(ImportError) as e:
            loader = _AnsibleInternalRedirectLoader('ansible.network.non_existent_module', [])
            assert 'not redirected, go ask path_hook' in str(e.value)
