
import pytest
from httpie.manager.tasks.plugins import PluginInstaller
from unittest.mock import patch, MagicMock
from pathlib import Path
import shutil
from collections import defaultdict
from pip._internal.utils.misc import get_site_paths
from pip._vendor.pep503 import PEP_503

@pytest.fixture(scope="module")
def mock_environment():
    env = MagicMock()
    env.config.plugins_dir = Path("/fake/plugin/directory")
    return env

@pytest.mark.parametrize("targets", [["plugin1-1.0"], ["plugin2-2.0"]])
def test_valid_inputs(mock_environment, targets):
    with patch('httpie.manager.tasks.plugins.get_site_paths', return_value=[Path("/fake/plugin/directory")]):
        installer = PluginInstaller(env=mock_environment)
        installer._clear_metadata(targets)

    for target in targets:
        name, _, version = target.rpartition('-')
        site_dir = Path("/fake/plugin/directory") / f"{name.replace('-', '_').lower().replace('-', '_')}"
        if version != "1.0" and version != "2.0":
            assert not Path(site_dir).exists()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_inputs.py:8:0: E0611: No name 'get_site_paths' in module 'pip._internal.utils.misc' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_inputs.py:9:0: E0401: Unable to import 'pip._vendor.pep503' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_inputs.py:9:0: E0611: No name 'pep503' in module 'pip._vendor' (no-name-in-module)


"""