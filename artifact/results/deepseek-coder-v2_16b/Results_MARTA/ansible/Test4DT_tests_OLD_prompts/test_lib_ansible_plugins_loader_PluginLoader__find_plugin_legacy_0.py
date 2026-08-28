
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import PluginLoader

def test_invalid_inputs():
    with patch('ansible.plugins.loader.PluginLoader', autospec=True):
        with pytest.raises(Exception):  # Adjust the exception type as per expected error handling in PluginLoader
            loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')
            loader._find_plugin_legacy('non_existent_plugin', MagicMock())
