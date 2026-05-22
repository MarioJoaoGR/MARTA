
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
def test_valid_input(mock_environment, targets):
    installer = PluginInstaller(env=mock_environment)
    
    with patch('httpie.manager.tasks.plugins.get_site_paths', return_value=[Path("/fake/plugin/directory")]):
        installer._clear_metadata(targets)
        
        result_deps = defaultdict(list)
        for site_dir in get_site_paths(installer.dir):
            for child in site_dir.iterdir():
                if child.suffix in {'.dist-info', '.egg-info'}:
                    name, _, version = child.stem.rpartition('-')
                    result_deps[name].append((version, child))
        
        for target in targets:
            name, _, version = target.rpartition('-')
            name = PEP_503.sub("-", name).lower().replace('-', '_')
            if name not in result_deps:
                continue
            
            for result_version, meta_path in result_deps[name]:
                if version != result_version:
                    assert not meta_path.exists(), f"Metadata file {meta_path} was not removed."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.py:8:0: E0611: No name 'get_site_paths' in module 'pip._internal.utils.misc' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.py:9:0: E0401: Unable to import 'pip._vendor.pep503' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.py:9:0: E0611: No name 'pep503' in module 'pip._vendor' (no-name-in-module)


"""