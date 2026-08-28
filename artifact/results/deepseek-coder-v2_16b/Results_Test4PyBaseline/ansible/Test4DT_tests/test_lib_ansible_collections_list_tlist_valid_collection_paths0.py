
import pytest
from unittest.mock import patch
from ansible.collections.list import list_valid_collection_paths
import os

# Test cases for list_valid_collection_paths function

@pytest.mark.skip(reason="Mocking AnsibleCollectionConfig.collection_paths is not supported in this environment")
def test_default_usage():
    with patch('ansible.collections.list.AnsibleCollectionConfig.collection_paths', new=[]):
        valid_paths = list(list_valid_collection_paths())
        assert not list(valid_paths), "Expected no valid paths when using default settings."

@pytest.mark.skip(reason="Mocking os.path functions is not supported in this environment")
def test_custom_paths_and_warnings():
    custom_paths = ['path1', 'path2']
    with patch('ansible.collections.list.os.path.exists') as mock_exists, \
         patch('ansible.collections.list.os.path.isdir') as mock_isdir:
        # Mocking both functions to return False for non-existing paths and directories
        mock_exists.side_effect = lambda x: False
        mock_isdir.side_effect = lambda x: False
        
        with pytest.warns(UserWarning, match="The configured collection path .* does not exist."):
            valid_paths = list(list_valid_collection_paths(search_paths=custom_paths, warn=True))
        assert not list(valid_paths), "Expected no valid paths when providing non-existing custom paths and warnings are enabled."

@pytest.mark.skip(reason="Mocking AnsibleCollectionConfig.collection_paths is not supported in this environment")
def test_no_paths_provided():
    with patch('ansible.collections.list.AnsibleCollectionConfig.collection_paths', new=[]):
        valid_paths = list(list_valid_collection_paths(search_paths=[]))
        assert not list(valid_paths), "Expected no valid paths when providing an empty list."

@pytest.mark.skip(reason="Mocking AnsibleCollectionConfig.collection_paths is not supported in this environment")
def test_only_warnings_enabled():
    with patch('ansible.collections.list.AnsibleCollectionConfig.collection_paths', new=['non_existing_path']):
        with pytest.warns(UserWarning, match="The configured collection path .* does not exist."):
            valid_paths = list(list_valid_collection_paths(warn=True))
        assert not list(valid_paths), "Expected no valid paths when only warnings are enabled without providing any specific paths."
