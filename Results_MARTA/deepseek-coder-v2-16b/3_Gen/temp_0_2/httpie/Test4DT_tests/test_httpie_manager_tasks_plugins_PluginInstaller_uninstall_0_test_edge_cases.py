
import unittest.mock as mock
from httpie.manager.tasks.plugins import PluginInstaller, ExitStatus

def test_uninstall():
    with mock.patch('httpie.manager.tasks.plugins.PluginInstaller._uninstall') as mock_uninstall:
        # Set up the mock to return a specific result for testing
        mock_uninstall.return_value = ExitStatus.SUCCESS
        
        installer = PluginInstaller(env=mock.Mock(), debug=False)
        targets = ["plugin1", "plugin2"]
        result = installer.uninstall(targets)
        
        # Check that _uninstall was called for each target
        assert mock_uninstall.call_count == len(targets)
        
        # Since all mocks return ExitStatus.SUCCESS, the final result should be SUCCESS
        assert result == ExitStatus.SUCCESS
