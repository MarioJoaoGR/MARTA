
import pytest
from shell_module import ShellModule

# Create an instance of ShellModule for PowerShell
@pytest.fixture(scope="function")
def shell_module():
    return ShellModule()

# Test case to check if a path has a trailing slash (Unix-like)
def test_path_has_trailing_slash_unix_like(shell_module):
    result1 = shell_module.path_has_trailing_slash("C:/path/to/file")
    assert not result1, "Expected False for Unix-like path without trailing slash"
    
    result2 = shell_module.path_has_trailing_slash("C:/path/to/file/")
    assert result2, "Expected True for Unix-like path with trailing slash"

# Test case to check if a Windows path has a trailing slash
def test_path_has_trailing_slash_windows(shell_module):
    result3 = shell_module.path_has_trailing_slash("C:\\path\\to\\file")
    assert result3, "Expected True for Windows path with trailing slash"
    
    result4 = shell_module.path_has_trailing_slash("C:\\path\\to\\file\\")
    assert not result4, "Expected False for Windows path without trailing slash"

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
_ ERROR collecting test_lib_ansible_plugins_shell_powershell_ShellModule_path_has_trailing_slash_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_path_has_trailing_slash_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_path_has_trailing_slash_0.py:3: in <module>
    from shell_module import ShellModule
E   ModuleNotFoundError: No module named 'shell_module'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_path_has_trailing_slash_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.37s ===============================
"""