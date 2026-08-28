
import pytest
from unittest.mock import patch
import os
from ansible.plugins.shell.powershell import ShellModule

class TestShellModule:
    
    @classmethod
    def setup_class(cls):
        cls.shell_module = ShellModule()
    
    def test_edge_cases(self):
        with pytest.raises(TypeError):
            self.shell_module.get_remote_filename(None)
    
    @patch('os.path.basename', return_value='script.exe')
    def test_invalid_input(self, mock_basename):
        result = self.shell_module.get_remote_filename("C:\\path\\to\\script.exe")
        assert result == 'script.exe'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_______________________ TestShellModule.test_edge_cases ________________________

self = <test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.TestShellModule object at 0x7ff555a3d750>

    def test_edge_cases(self):
        with pytest.raises(TypeError):
>           self.shell_module.get_remote_filename(None)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.shell.powershell.ShellModule object at 0x7ff555a3f640>
pathname = None

    def get_remote_filename(self, pathname):
        # powershell requires that script files end with .ps1
>       base_name = os.path.basename(pathname.strip())
E       AttributeError: 'NoneType' object has no attribute 'strip'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/shell/powershell.py:92: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py::TestShellModule::test_edge_cases
========================= 1 failed, 1 passed in 0.39s ==========================
"""