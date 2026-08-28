
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

# Test case for get_all_plugins_of_type function with a valid plugin type

# Test case for get_all_plugins_of_type function with an invalid plugin type
def test_get_all_plugins_of_type_invalid():
    with patch('ansible.cli.doc.plugin_loader') as mock_plugin_loader:
        # Mocking _get_paths_with_context to return a list of path contexts
        mock_plugin_loader.return_value._get_paths_with_context = MagicMock(return_value=[MagicMock(path='/mocked/path', internal=True)])
        
        # Mocking find_plugins to return an empty set
        mock_plugin_loader.return_value.find_plugins = MagicMock(return_value={})
        
        # Calling the function under test
        plugin_list = DocCLI.get_all_plugins_of_type('invalid_type')
        
        # Assertions to validate the results
        assert isinstance(plugin_list, list)
        assert len(plugin_list) == 0