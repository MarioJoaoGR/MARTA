
import os
from ansible.plugins.shell.powershell import ShellModule
import pytest

@pytest.fixture(scope="module")
def shell_module():
    return ShellModule()



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________ test_get_remote_filename_with_no_extension __________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7fc35c4c88e0>

    def test_get_remote_filename_with_no_extension(shell_module):
        result = shell_module.get_remote_filename("C:\\path\\to\\script")
>       assert result == 'script.ps1'
E       AssertionError: assert 'C:\\path\\to\\script.ps1' == 'script.ps1'
E         
E         - script.ps1
E         + C:\path\to\script.ps1

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py:12: AssertionError
_________________ test_get_remote_filename_with_exe_extension __________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7fc35c4c88e0>

    def test_get_remote_filename_with_exe_extension(shell_module):
        result = shell_module.get_remote_filename("C:\\path\\to\\script.exe")
>       assert result == 'script.exe'
E       AssertionError: assert 'C:\\path\\to\\script.exe' == 'script.exe'
E         
E         - script.exe
E         + C:\path\to\script.exe

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py:16: AssertionError
_________________ test_get_remote_filename_with_ps1_extension __________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7fc35c4c88e0>

    def test_get_remote_filename_with_ps1_extension(shell_module):
        result = shell_module.get_remote_filename("C:\\path\\to\\script.ps1")
>       assert result == 'script.ps1'
E       AssertionError: assert 'C:\\path\\to\\script.ps1' == 'script.ps1'
E         
E         - script.ps1
E         + C:\path\to\script.ps1

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py::test_get_remote_filename_with_no_extension
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py::test_get_remote_filename_with_exe_extension
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_get_remote_filename_0.py::test_get_remote_filename_with_ps1_extension
============================== 3 failed in 0.43s ===============================
"""