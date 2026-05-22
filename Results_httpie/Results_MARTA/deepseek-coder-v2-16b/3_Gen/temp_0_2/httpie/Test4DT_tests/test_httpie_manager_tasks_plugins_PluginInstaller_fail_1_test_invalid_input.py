
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller
from httpie.manager.core import Environment, ExitStatus

class TestPluginInstaller(unittest.TestCase):
    @patch('httpie.manager.tasks.plugins.Environment')
    def test_fail(self, MockEnvironment):
        # Arrange
        mock_env = MockEnvironment.return_value
        installer = PluginInstaller(mock_env)
        
        command = "install"
        target = "plugin_name"
        reason = "not found"
        
        expected_message = f'Can\'t {command} {target!r}: {reason}'
        
        # Act
        result = installer.fail(command, target, reason)
        
        # Assert
        mock_env.stderr.write.assert_called_with(expected_message + '\n')
        self.assertEqual(result, ExitStatus.ERROR)
