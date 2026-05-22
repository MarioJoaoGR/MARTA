
import unittest.mock as mock
from httpie.manager.tasks.plugins import PluginInstaller

def test_invalid_target():
    with mock.patch('httpie.manager.tasks.plugins.importlib_metadata') as mock_importlib_metadata:
        mock_importlib_metadata.distribution.side_effect = importlib_metadata.PackageNotFoundError()
        
        env = mock.MagicMock()
        installer = PluginInstaller(env=env)
        
        result = installer._uninstall("invalid_target")
        
        assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__uninstall_0_test_invalid_target.py:7:59: E0602: Undefined variable 'importlib_metadata' (undefined-variable)


"""