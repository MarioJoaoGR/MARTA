
import pytest
from unittest.mock import patch
from ansible.plugins.shell.powershell import ShellModule

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_chown_0.py F [100%]

=================================== FAILURES ===================================
___________________________ test_chown_method_mocked ___________________________

    def test_chown_method_mocked():
        with patch('ansible.plugins.shell.powershell.ShellModule') as MockShellModule:
            mock_instance = MockShellModule.return_value
>           with pytest.raises(NotImplementedError):
E           Failed: DID NOT RAISE <class 'NotImplementedError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_chown_0.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_chown_0.py::test_chown_method_mocked
============================== 1 failed in 0.38s ===============================
"""