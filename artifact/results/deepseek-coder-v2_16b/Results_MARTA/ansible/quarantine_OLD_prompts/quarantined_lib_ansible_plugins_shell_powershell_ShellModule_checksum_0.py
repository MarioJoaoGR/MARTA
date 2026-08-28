
import pytest
from unittest.mock import patch
import base64
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_checksum_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_path_file _____________________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f1cec92f1f0>

    def test_valid_path_file(shell_module):
        with patch('ansible.plugins.shell.powershell.ShellModule._encode_script', return_value=base64.b64encode("test_script".encode()).decode()):
            script = shell_module.checksum('example.txt')
            assert isinstance(script, str)
>           assert base64.b64decode(script).decode().startswith("$sp")  # Check if it's a PowerShell script for SHA1 checksum
E           AssertionError: assert False
E            +  where False = <built-in method startswith of str object at 0x7f1cece90630>('$sp')
E            +    where <built-in method startswith of str object at 0x7f1cece90630> = 'test_script'.startswith
E            +      where 'test_script' = <built-in method decode of bytes object at 0x7f1cec6d90b0>()
E            +        where <built-in method decode of bytes object at 0x7f1cec6d90b0> = b'test_script'.decode
E            +          where b'test_script' = <function b64decode at 0x7f1ceddef6d0>('dGVzdF9zY3JpcHQ=')
E            +            where <function b64decode at 0x7f1ceddef6d0> = base64.b64decode

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_checksum_0.py:15: AssertionError
__________________________ test_valid_path_directory ___________________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f1cec6dbd60>

    def test_valid_path_directory(shell_module):
        with patch('ansible.plugins.shell.powershell.ShellModule._encode_script', return_value=base64.b64encode("test_script".encode()).decode()):
            script = shell_module.checksum('example_dir')
            assert isinstance(script, str)
>           assert base64.b64decode(script).decode().startswith("$sp")  # Check if it's a PowerShell script for directory check
E           AssertionError: assert False
E            +  where False = <built-in method startswith of str object at 0x7f1ced04b270>('$sp')
E            +    where <built-in method startswith of str object at 0x7f1ced04b270> = 'test_script'.startswith
E            +      where 'test_script' = <built-in method decode of bytes object at 0x7f1cec6d9d70>()
E            +        where <built-in method decode of bytes object at 0x7f1cec6d9d70> = b'test_script'.decode
E            +          where b'test_script' = <function b64decode at 0x7f1ceddef6d0>('dGVzdF9zY3JpcHQ=')
E            +            where <function b64decode at 0x7f1ceddef6d0> = base64.b64decode

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_checksum_0.py:21: AssertionError
______________________________ test_invalid_path _______________________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f1cec6d9c60>

    def test_invalid_path(shell_module):
        with patch('ansible.plugins.shell.powershell.ShellModule._encode_script', return_value=base64.b64encode("test_script".encode()).decode()):
            script = shell_module.checksum('nonexistent')
            assert isinstance(script, str)
>           assert base64.b64decode(script).decode().startswith("$sp")  # Check if it's a PowerShell script for path existence check
E           AssertionError: assert False
E            +  where False = <built-in method startswith of str object at 0x7f1cec7151b0>('$sp')
E            +    where <built-in method startswith of str object at 0x7f1cec7151b0> = 'test_script'.startswith
E            +      where 'test_script' = <built-in method decode of bytes object at 0x7f1cec643570>()
E            +        where <built-in method decode of bytes object at 0x7f1cec643570> = b'test_script'.decode
E            +          where b'test_script' = <function b64decode at 0x7f1ceddef6d0>('dGVzdF9zY3JpcHQ=')
E            +            where <function b64decode at 0x7f1ceddef6d0> = base64.b64decode

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_checksum_0.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_checksum_0.py::test_valid_path_file
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_checksum_0.py::test_valid_path_directory
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_checksum_0.py::test_invalid_path
============================== 3 failed in 0.41s ===============================
"""