
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input_tilde ____________________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f14228b81f0>

    def test_valid_input_tilde(shell_module):
        user_home_path = '~\Documents\Report.txt'
        expanded_path = shell_module.expand_user(user_home_path)
>       assert expanded_path == "C:\\Users\\username\\Documents\\Report.txt"  # Assuming the current user is 'username'
E       AssertionError: assert 'PowerShell -...AIAB9ACAAfQA=' == 'C:\\Users\\u...s\\Report.txt'
E         
E         - C:\Users\username\Documents\Report.txt
E         + PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZABlACAALQBWAGUAcgBzAGkAbwBuACAATABhAHQAZQBzAHQACgBXAHIAaQB0AGUALQBPAHUAdABwAHUAdAAgACgAKABHAGUAdAAtAEwAbwBjAGEAdABpAG8AbgApAC4AUABhAHQAaAAgACsAIAAnAFwARABvAGMAdQBtAGUAbgB0AHMAXABSAGUAcABvAHIAdAAuAHQAeAB0ACcAKQAKAEkAZgAgACgALQBuAG8AdAAgACQAPwApACAAewAgAEkAZgAgACgARwBlAHQALQBWAGEAcgBpAGEAYgBsAGUAIABMAEEAUwBUAEUAWABJAFQAQwBPAEQARQAgAC0ARQByAHIAbwByAEEAYwB0AGkAbwBuACAAUwBpAGwAZQBuAHQAbAB5AEMAbwBuAHQAaQBuAHUAZQApACAAew...
E         
E         ...Full output truncated (1 line hidden), use '-vv' to show

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py:12: AssertionError
_____________________________ test_edge_case_none ______________________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f14228b81f0>

    def test_edge_case_none(shell_module):
        user_home_path = None
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py:16: Failed
______________________ test_invalid_input_error_handling _______________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f14228b81f0>

    def test_invalid_input_error_handling(shell_module):
        user_home_path = 'InvalidInput'
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py:21: Failed
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py:10
  /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py:10: DeprecationWarning: invalid escape sequence '\D'
    user_home_path = '~\Documents\Report.txt'

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py::test_valid_input_tilde
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_expand_user_0.py::test_invalid_input_error_handling
========================= 3 failed, 1 warning in 0.43s =========================
"""