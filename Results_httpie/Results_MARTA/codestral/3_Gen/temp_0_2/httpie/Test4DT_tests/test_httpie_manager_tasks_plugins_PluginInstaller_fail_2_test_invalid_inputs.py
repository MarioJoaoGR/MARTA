
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, Environment, ExitStatus

@pytest.mark.parametrize("command, target, reason", [
    ("install", "plugin_name", "not found"),
    ("update", None, "permission denied"),
    ("remove", "plugin_dir", "directory not empty")
])
def test_invalid_inputs(command, target, reason):
    with patch('httpie.manager.tasks.plugins.Environment', autospec=True) as mock_env:
        mock_env_instance = mock_env.return_value
        mock_env_instance.config.plugins_dir = "mocked_plugin_dir"
        
        with patch('pathlib.Path.mkdir', side_effect=AttributeError("'str' object has no attribute 'mkdir'")):
            with pytest.raises(AttributeError):
                installer = PluginInstaller(env=mock_env_instance, debug=False)
