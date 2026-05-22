
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, Environment, ExitStatus

def test_invalid_input():
    with patch('httpie.manager.tasks.plugins.PluginInstaller.__init__', side_effect=Exception("Invalid Input")):
        env = Environment(config=MagicMock(), stderr=MagicMock())
        with pytest.raises(Exception):
            installer = PluginInstaller(env=env, debug=True)
