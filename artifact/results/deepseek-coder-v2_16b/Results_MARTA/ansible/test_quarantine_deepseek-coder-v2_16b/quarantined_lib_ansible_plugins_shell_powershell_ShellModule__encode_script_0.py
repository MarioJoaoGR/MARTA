
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture(scope="module")
def powershell_module():
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule__encode_script_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_encode_script_as_list __________________________

powershell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f4f01b584c0>

    def test_encode_script_as_list(powershell_module):
        script = "Write-Output 'Hello, World!'"
        result = powershell_module._encode_script(script, as_list=True)
        assert isinstance(result, list), f"Expected a list but got {type(result)}"
>       assert len(result) == 2, f"Expected list length to be 2 but got {len(result)}"
E       AssertionError: Expected list length to be 2 but got 7
E       assert 7 == 2
E        +  where 7 = len(['PowerShell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Unrestricted', '-EncodedCommand', ...])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule__encode_script_0.py:13: AssertionError
________________________ test_encode_script_strict_mode ________________________

powershell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f4f01b584c0>

    def test_encode_script_strict_mode(powershell_module):
        script = "Write-Output 'Hello, World!'"
        result = powershell_module._encode_script(script, strict_mode=True)
        assert isinstance(result, str), f"Expected a string but got {type(result)}"
        assert len(result) > 0, "Expected non-empty string"
>       assert "Set-StrictMode -Version Latest" in result, "Expected 'Set-StrictMode -Version Latest' to be in the encoded script"
E       AssertionError: Expected 'Set-StrictMode -Version Latest' to be in the encoded script
E       assert 'Set-StrictMode -Version Latest' in 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZ...BlACkAIAB7ACAAZQB4AGkAdAAgACQATABBAFMAVABFAFgASQBUAEMATwBEAEUAIAB9ACAARQBsAHMAZQAgAHsAIABlAHgAaQB0ACAAMQAgAH0AIAB9AA=='

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule__encode_script_0.py:20: AssertionError
________________________ test_encode_script_preserve_rc ________________________

powershell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f4f01b584c0>

    def test_encode_script_preserve_rc(powershell_module):
        script = "Write-Output 'Hello, World!'"
        result = powershell_module._encode_script(script, preserve_rc=True)
        assert isinstance(result, str), f"Expected a string but got {type(result)}"
        assert len(result) > 0, "Expected non-empty string"
        expected_string = "If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }\r\n"
>       assert expected_string in result, f"Expected '{expected_string}' to be in the encoded script"
E       AssertionError: Expected 'If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }
E         ' to be in the encoded script
E       assert 'If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }\r\n' in 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZ...BlACkAIAB7ACAAZQB4AGkAdAAgACQATABBAFMAVABFAFgASQBUAEMATwBEAEUAIAB9ACAARQBsAHMAZQAgAHsAIABlAHgAaQB0ACAAMQAgAH0AIAB9AA=='

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule__encode_script_0.py:28: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule__encode_script_0.py::test_encode_script_as_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule__encode_script_0.py::test_encode_script_strict_mode
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule__encode_script_0.py::test_encode_script_preserve_rc
============================== 3 failed in 0.45s ===============================
"""