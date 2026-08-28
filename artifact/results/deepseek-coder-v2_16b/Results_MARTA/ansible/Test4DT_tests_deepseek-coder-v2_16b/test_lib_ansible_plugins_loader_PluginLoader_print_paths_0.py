
import pytest
from ansible.plugins.loader import PluginLoader

def test_invalid_input():
    with pytest.raises(TypeError):
        loader = PluginLoader()  # This should raise a TypeError because __init__ expects at least one argument
