
import pytest
from ansible.plugins.shell.powershell import ShellModule
import pkgutil
import shlex
import os

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
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________ test_build_module_command_with_empty_cmd ___________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f818b489390>

    def test_build_module_command_with_empty_cmd(shell_module):
        env_string = "SomeEnvVar=value"
        shebang = "#!powershell"
        cmd = ""
        arg_path = None
    
        result = shell_module.build_module_command(env_string, shebang, cmd, arg_path)
    
        assert isinstance(result, str), "Expected a string representation of the command"
>       assert "bootstrap_wrapper.ps1" in result, "Expected the bootstrap wrapper script to be included"
E       AssertionError: Expected the bootstrap wrapper script to be included
E       assert 'bootstrap_wrapper.ps1' in 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand JgBjAGgAYwBwAC4AYwBvAG0AIAA2ADUAM...BjAGsAXQA6ADoAQwByAGUAYQB0AGUAKAAkAHMAcABsAGkAdABfAHAAYQByAHQAcwBbADAAXQApAAoAJgAkAGUAeABlAGMAXwB3AHIAYQBwAHAAZQByAA=='

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_1.py:21: AssertionError
_________________ test_build_module_command_with_non_empty_cmd _________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f818b489390>

    def test_build_module_command_with_non_empty_cmd(shell_module):
        env_string = "SomeEnvVar=value"
        shebang = "#!powershell"
        cmd = "Write-Output 'Hello, World!'"
        arg_path = None
    
        result = shell_module.build_module_command(env_string, shebang, cmd, arg_path)
    
        assert isinstance(result, str), "Expected a string representation of the command"
>       assert cmd in result, "Expected the provided command to be included"
E       AssertionError: Expected the provided command to be included
E       assert "Write-Output 'Hello, World!'" in 'type "Write-Output.ps1" | PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand JgBjAGg...BjAGsAXQA6ADoAQwByAGUAYQB0AGUAKAAkAHMAcABsAGkAdABfAHAAYQByAHQAcwBbADAAXQApAAoAJgAkAGUAeABlAGMAXwB3AHIAYQBwAHAAZQByAA=='

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_1.py:32: AssertionError
________________ test_build_module_command_with_shebang_and_cmd ________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f818b489390>

    def test_build_module_command_with_shebang_and_cmd(shell_module):
        env_string = "SomeEnvVar=value"
        shebang = "#!powershell"
        cmd = "Write-Output 'Hello, World!'"
        arg_path = None
    
        result = shell_module.build_module_command(env_string, shebang, cmd, arg_path)
    
        assert isinstance(result, str), "Expected a string representation of the command"
>       assert cmd in result, "Expected the provided command to be included"
E       AssertionError: Expected the provided command to be included
E       assert "Write-Output 'Hello, World!'" in 'type "Write-Output.ps1" | PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand JgBjAGg...BjAGsAXQA6ADoAQwByAGUAYQB0AGUAKAAkAHMAcABsAGkAdABfAHAAYQByAHQAcwBbADAAXQApAAoAJgAkAGUAeABlAGMAXwB3AHIAYQBwAHAAZQByAA=='

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_1.py:43: AssertionError
_________________ test_build_module_command_with_binary_module _________________

shell_module = <ansible.plugins.shell.powershell.ShellModule object at 0x7f818b489390>

    def test_build_module_command_with_binary_module(shell_module):
        env_string = "SomeEnvVar=value"
        shebang = None
        cmd = "script.exe arg1 arg2"
        arg_path = None
    
>       result = shell_module.build_module_command(env_string, shebang, cmd, arg_path)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_1.py:51: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.shell.powershell.ShellModule object at 0x7f818b489390>
env_string = 'SomeEnvVar=value', shebang = None, cmd = 'script.exe arg1 arg2'
arg_path = None

    def build_module_command(self, env_string, shebang, cmd, arg_path=None):
        bootstrap_wrapper = pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1")
    
        # pipelining bypass
        if cmd == '':
            return self._encode_script(script=bootstrap_wrapper, strict_mode=False, preserve_rc=False)
    
        # non-pipelining
    
        cmd_parts = shlex.split(cmd, posix=False)
        cmd_parts = list(map(to_text, cmd_parts))
        if shebang and shebang.lower() == '#!powershell':
            if not self._unquote(cmd_parts[0]).lower().endswith('.ps1'):
                # we're running a module via the bootstrap wrapper
                cmd_parts[0] = '"%s.ps1"' % self._unquote(cmd_parts[0])
            wrapper_cmd = "type " + cmd_parts[0] + " | " + self._encode_script(script=bootstrap_wrapper, strict_mode=False, preserve_rc=False)
            return wrapper_cmd
        elif shebang and shebang.startswith('#!'):
            cmd_parts.insert(0, shebang[2:])
        elif not shebang:
            # The module is assumed to be a binary
            cmd_parts[0] = self._unquote(cmd_parts[0])
            cmd_parts.append(arg_path)
        script = '''
            Try
            {
                %s
                %s
            }
            Catch
            {
                $_obj = @{ failed = $true }
                If ($_.Exception.GetType)
                {
                    $_obj.Add('msg', $_.Exception.Message)
                }
                Else
                {
                    $_obj.Add('msg', $_.ToString())
                }
                If ($_.InvocationInfo.PositionMessage)
                {
                    $_obj.Add('exception', $_.InvocationInfo.PositionMessage)
                }
                ElseIf ($_.ScriptStackTrace)
                {
                    $_obj.Add('exception', $_.ScriptStackTrace)
                }
                Try
                {
                    $_obj.Add('error_record', ($_ | ConvertTo-Json | ConvertFrom-Json))
                }
                Catch
                {
                }
                Echo $_obj | ConvertTo-Json -Compress -Depth 99
                Exit 1
            }
>       ''' % (env_string, ' '.join(cmd_parts))
E       TypeError: sequence item 3: expected str instance, NoneType found

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/shell/powershell.py:243: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_1.py::test_build_module_command_with_empty_cmd
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_1.py::test_build_module_command_with_non_empty_cmd
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_1.py::test_build_module_command_with_shebang_and_cmd
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_1.py::test_build_module_command_with_binary_module
============================== 4 failed in 0.79s ===============================
"""