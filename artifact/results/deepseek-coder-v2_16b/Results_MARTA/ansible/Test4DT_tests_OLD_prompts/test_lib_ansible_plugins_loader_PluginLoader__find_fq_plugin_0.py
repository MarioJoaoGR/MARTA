
import pytest
from ansible.plugins.loader import PluginLoader

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # This should raise a TypeError because the constructor does not accept positional arguments
        loader = PluginLoader()
