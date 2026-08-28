
import pytest
from ansible.plugins.loader import PluginLoader


def test_invalid_input():
    with pytest.raises(TypeError):
        PluginLoader()