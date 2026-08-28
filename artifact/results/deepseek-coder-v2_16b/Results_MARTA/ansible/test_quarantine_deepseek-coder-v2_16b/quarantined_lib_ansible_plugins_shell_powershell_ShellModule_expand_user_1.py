
import pytest
from ansible.plugins.shell.powershell import ShellModule

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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_ShellModule_expand_user_basic ______________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f7590cf6320>

    def test_ShellModule_expand_user_basic(shell_module):
        # Test expanding a path containing '~' to the user's home directory
        expanded_path = shell_module.expand_user('~\Documents\Report.txt')
>       assert expanded_path == "C:\\Users\\username\\Documents\\Report.txt"  # Assuming the current user is 'username'
E       AssertionError: assert 'PowerShell -...AIAB9ACAAfQA=' == 'C:\\Users\\u...s\\Report.txt'
E         
E         - C:\Users\username\Documents\Report.txt
E         + PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZABlACAALQBWAGUAcgBzAGkAbwBuACAATABhAHQAZQBzAHQACgBXAHIAaQB0AGUALQBPAHUAdABwAHUAdAAgACgAKABHAGUAdAAtAEwAbwBjAGEAdABpAG8AbgApAC4AUABhAHQAaAAgACsAIAAnAFwARABvAGMAdQBtAGUAbgB0AHMAXABSAGUAcABvAHIAdAAuAHQAeAB0ACcAKQAKAEkAZgAgACgALQBuAG8AdAAgACQAPwApACAAewAgAEkAZgAgACgARwBlAHQALQBWAGEAcgBpAGEAYgBsAGUAIABMAEEAUwBUAEUAWABJAFQAQwBPAEQARQAgAC0ARQByAHIAbwByAEEAYwB0AGkAbwBuACAAUwBpAGwAZQBuAHQAbAB5AEMAbwBuAHQAaQBuAHUAZQApACAAew...
E         
E         ...Full output truncated (1 line hidden), use '-vv' to show

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py:12: AssertionError
____________________ test_ShellModule_expand_absolute_path _____________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f7590cf6320>

    def test_ShellModule_expand_absolute_path(shell_module):
        # Test expanding an absolute path without expansion needed
        absolute_path = shell_module.expand_user('C:\Program Files\SomeFile.txt')
>       assert absolute_path == "C:\\Program Files\\SomeFile.txt"
E       AssertionError: assert 'PowerShell -...xACAAfQAgAH0A' == 'C:\\Program ...\SomeFile.txt'
E         
E         - C:\Program Files\SomeFile.txt
E         + PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZABlACAALQBWAGUAcgBzAGkAbwBuACAATABhAHQAZQBzAHQACgBXAHIAaQB0AGUALQBPAHUAdABwAHUAdAAgACcAQwA6AFwAUAByAG8AZwByAGEAbQAgAEYAaQBsAGUAcwBcAFMAbwBtAGUARgBpAGwAZQAuAHQAeAB0ACcACgBJAGYAIAAoAC0AbgBvAHQAIAAkAD8AKQAgAHsAIABJAGYAIAAoAEcAZQB0AC0AVgBhAHIAaQBhAGIAbABlACAATABBAFMAVABFAFgASQBUAEMATwBEAEUAIAAtAEUAcgByAG8AcgBBAGMAdABpAG8AbgAgAFMAaQBsAGUAbgB0AGwAeQBDAG8AbgB0AGkAbgB1AGUAKQAgAHsAIABlAHgAaQB0ACAAJABMAEEAUwBUAEUAWABJAFQAQwBPAEQARQAgAH0AIABFAGwAcwBlACAAewAgAGUAeABpAHQAIAAxACAAfQAgAH0A

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py:17: AssertionError
____________________ test_ShellModule_expand_unchanged_path ____________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f7590cf6320>

    def test_ShellModule_expand_unchanged_path(shell_module):
        # Test expanding a path without a tilde present
        unchanged_path = shell_module.expand_user('Documents\Report.txt')
>       assert unchanged_path == "Documents\\Report.txt"
E       AssertionError: assert 'PowerShell -...xACAAfQAgAH0A' == 'Documents\\Report.txt'
E         
E         - Documents\Report.txt
E         + PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZABlACAALQBWAGUAcgBzAGkAbwBuACAATABhAHQAZQBzAHQACgBXAHIAaQB0AGUALQBPAHUAdABwAHUAdAAgACcARABvAGMAdQBtAGUAbgB0AHMAXABSAGUAcABvAHIAdAAuAHQAeAB0ACcACgBJAGYAIAAoAC0AbgBvAHQAIAAkAD8AKQAgAHsAIABJAGYAIAAoAEcAZQB0AC0AVgBhAHIAaQBhAGIAbABlACAATABBAFMAVABFAFgASQBUAEMATwBEAEUAIAAtAEUAcgByAG8AcgBBAGMAdABpAG8AbgAgAFMAaQBsAGUAbgB0AGwAeQBDAG8AbgB0AGkAbgB1AGUAKQAgAHsAIABlAHgAaQB0ACAAJABMAEEAUwBUAEUAWABJAFQAQwBPAEQARQAgAH0AIABFAGwAcwBlACAAewAgAGUAeABpAHQAIAAxACAAfQAgAH0A

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py:22: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py:11
  /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py:11: DeprecationWarning: invalid escape sequence '\D'
    expanded_path = shell_module.expand_user('~\Documents\Report.txt')

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py:16
  /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py:16: DeprecationWarning: invalid escape sequence '\P'
    absolute_path = shell_module.expand_user('C:\Program Files\SomeFile.txt')

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py:21
  /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py:21: DeprecationWarning: invalid escape sequence '\R'
    unchanged_path = shell_module.expand_user('Documents\Report.txt')

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py::test_ShellModule_expand_user_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py::test_ShellModule_expand_absolute_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_1.py::test_ShellModule_expand_unchanged_path
======================== 3 failed, 3 warnings in 0.77s =========================
"""