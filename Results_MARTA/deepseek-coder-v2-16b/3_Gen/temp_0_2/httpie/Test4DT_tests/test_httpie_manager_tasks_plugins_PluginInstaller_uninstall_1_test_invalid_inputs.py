
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, Environment, ExitStatus

def test_invalid_inputs():
    # Test error handling with invalid inputs like non-string values or unsupported types
    
    env = Environment()
    
    with pytest.raises(TypeError):
        # Passing a non-string value to targets should raise TypeError
        PluginInstaller(env, debug=True).uninstall([123])
        
    with pytest.raises(TypeError):
        # Passing a list containing a non-string value should raise TypeError
        PluginInstaller(env, debug=True).uninstall(["plugin1", 123])
        
    with pytest.raises(ValueError):
        # Passing an empty string to targets should raise ValueError
        PluginInstaller(env, debug=True).uninstall([""])
