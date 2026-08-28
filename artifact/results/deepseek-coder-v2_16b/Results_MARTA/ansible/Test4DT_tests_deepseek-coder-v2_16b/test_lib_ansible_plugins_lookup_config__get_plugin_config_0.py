
import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleLookupError, AnsibleError
from ansible.plugins.lookup.config import _get_plugin_config


def test_invalid_plugin():
    # Setup: Real instance of plugin_loader with minimal args
    loader = MagicMock()
    loader.get = MagicMock(return_value=None)
    
    with pytest.raises(AnsibleLookupError):
        config_settings = _get_plugin_config('my_lookup', 'lookup', {'key': 'value'}, {'var1': 'val1'})

def test_missing_setting():
    # Setup: Real instance of plugin_loader with minimal args
    loader = MagicMock()
    loader.get = MagicMock(return_value=MagicMock())
    
    with patch('ansible.plugins.lookup.config._get_plugin_config', side_effect=AnsibleError("Setting was not defined")):
        with pytest.raises(AnsibleError):
            config_settings = _get_plugin_config('my_lookup', 'lookup', {'key': 'value'}, {'var1': 'val1'})