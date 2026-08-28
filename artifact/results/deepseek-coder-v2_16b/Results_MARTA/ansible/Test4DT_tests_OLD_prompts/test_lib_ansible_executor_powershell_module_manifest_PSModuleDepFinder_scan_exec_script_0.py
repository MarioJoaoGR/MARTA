
import pytest
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from unittest.mock import patch, MagicMock



def test_existing_script():
    with patch('pkgutil.get_data', return_value=b'mocked data'):
        finder = PSModuleDepFinder()
        finder.scan_exec_script("ExistingScript")
        assert "ExistingScript" in finder.exec_scripts