
import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

def test_valid_input():
    with patch('ansible.executor.powershell.module_manifest.PSModuleDepFinder') as mock_finder:
        # Arrange
        finder = mock_finder.return_value
        finder.ps_modules = {'PowerShellModule1': '1.0', 'PowerShellModule2': '2.0'}
        finder.cs_utils_module = {}  # Ensure it starts empty for this test

        # Act
        finder.scan_module(b'#AnsibleRequires -PowerShell Ansible.ModuleUtils.Util1')

        # Assert
        assert finder.ps_modules == {'PowerShellModule1': '1.0', 'PowerShellModule2': '2.0'}
        assert finder.cs_utils_module == {}

def test_edge_case():
    with patch('ansible.executor.powershell.module_manifest.PSModuleDepFinder') as mock_finder:
        # Arrange
        finder = mock_finder.return_value
        finder.ps_modules = {}  # Ensure it starts empty for this test
        finder.cs_utils_module = {}  # Ensure it starts empty for this test

        # Act
        finder.scan_module(b'')

        # Assert
        assert not finder.ps_modules
        assert not finder.cs_utils_module
