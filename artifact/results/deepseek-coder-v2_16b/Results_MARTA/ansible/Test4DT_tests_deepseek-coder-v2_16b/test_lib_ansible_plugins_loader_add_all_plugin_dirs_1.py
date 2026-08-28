
import pytest
import os
from ansible.plugins.loader import add_all_plugin_dirs
from unittest.mock import patch, MagicMock

def test_none_input():
    with patch('ansible.plugins.loader.display') as mock_display:
        # Call the function with None
        add_all_plugin_dirs(None)
        assert mock_display.call_count == 0, "Expected no call to display"


def test_valid_directory():
    with patch('ansible.plugins.loader.os.path.isdir', return_value=True) as mock_isdir, \
         patch('ansible.plugins.loader.get_all_plugin_loaders') as mock_get_all_plugin_loaders, \
         patch('ansible.plugins.loader.display') as mock_display:
        # Call the function with a valid directory path
        add_all_plugin_dirs('/valid/path/to/plugins')
        assert mock_isdir.call_count == 1, "Expected one call to os.path.isdir"
        assert mock_get_all_plugin_loaders.call_count == 1, "Expected one call to get_all_plugin_loaders"
        assert mock_display.call_count == 0, "Expected no calls to display for valid path"