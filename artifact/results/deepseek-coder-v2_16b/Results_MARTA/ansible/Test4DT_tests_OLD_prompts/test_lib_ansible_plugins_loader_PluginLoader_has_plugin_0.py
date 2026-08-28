
import pytest
from unittest.mock import patch
from ansible.plugins.loader import PluginLoader



def test_invalid_input():
    with pytest.raises(TypeError):
        PluginLoader()