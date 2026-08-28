
import pytest
from ansible.plugins.shell.powershell import ShellModule
import pkgutil
import shlex
import to_text

@pytest.fixture
def shell_module():
    return ShellModule()

def test_build_module_command_with_cmd(shell_module):
    cmd = shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="Write-Output 'Hello, World!'")
    assert isinstance(cmd, str)
    assert "SomeEnvVar=value" in cmd
    assert "#!powershell" in cmd
    assert "Write-Output 'Hello, World!'" in cmd

def test_build_module_command_with_empty_cmd(shell_module):
    cmd = shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="")
    assert isinstance(cmd, str)
    assert "SomeEnvVar=value" in cmd
    assert "#!powershell" in cmd
    assert pkgutil.get_data("ansible.executor.powershell", "bootstrap_wrapper.ps1").decode() in cmd

def test_build_module_command_with_non_pipelined_cmd(shell_module):
    cmd = shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="Write-Output 'Hello, World!'")
    assert isinstance(cmd, str)
    assert "SomeEnvVar=value" in cmd
    assert "#!powershell" in cmd
    assert "Write-Output 'Hello, World!'" in cmd

def test_build_module_command_with_binary_module(shell_module):
    cmd = shell_module.build_module_command(env_string="SomeEnvVar=value", shebang=None, cmd="script.exe arg1 arg2")
    assert isinstance(cmd, str)
    assert "SomeEnvVar=value" in cmd
    assert script_parts[0] == '"script.exe"'  # This part is hypothetical as the actual command construction logic might differ
    assert "arg1 arg2" in cmd

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py:6: in <module>
    import to_text
E   ModuleNotFoundError: No module named 'to_text'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.48s ===============================
"""