
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="function")
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_remove_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_remove_file_without_recursion ______________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f3b94c10310>

    def test_remove_file_without_recursion(shell_module):
        with pytest.raises(FileNotFoundError):
            result = shell_module.remove("non_existent_file.txt")
>           assert not result  # This will fail if the command does not raise FileNotFoundError
E           AssertionError: assert not 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZ...BlACkAIAB7ACAAZQB4AGkAdAAgACQATABBAFMAVABFAFgASQBUAEMATwBEAEUAIAB9ACAARQBsAHMAZQAgAHsAIABlAHgAaQB0ACAAMQAgAH0AIAB9AA=='

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_remove_0.py:12: AssertionError
_____________________ test_remove_directory_with_recursion _____________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f3b94bfc490>

    def test_remove_directory_with_recursion(shell_module):
        with pytest.raises(FileNotFoundError):
            result = shell_module.remove("non_existent_directory", recurse=True)
>           assert not result  # This will fail if the command does not raise FileNotFoundError
E           AssertionError: assert not 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZ...B1AGUAKQAgAHsAIABlAHgAaQB0ACAAJABMAEEAUwBUAEUAWABJAFQAQwBPAEQARQAgAH0AIABFAGwAcwBlACAAewAgAGUAeABpAHQAIAAxACAAfQAgAH0A'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_remove_0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_remove_0.py::test_remove_file_without_recursion
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_remove_0.py::test_remove_directory_with_recursion
============================== 2 failed in 0.40s ===============================
"""