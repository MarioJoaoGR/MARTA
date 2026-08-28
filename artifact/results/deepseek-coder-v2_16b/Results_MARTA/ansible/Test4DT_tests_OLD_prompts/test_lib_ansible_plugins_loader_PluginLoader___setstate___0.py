
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import PluginLoader, MODULE_CACHE, PATH_CACHE, PLUGIN_PATH_CACHE


def test_invalid_inputs():
    with pytest.raises(TypeError):
        PluginLoader()  # This should raise a TypeError because not enough arguments are provided