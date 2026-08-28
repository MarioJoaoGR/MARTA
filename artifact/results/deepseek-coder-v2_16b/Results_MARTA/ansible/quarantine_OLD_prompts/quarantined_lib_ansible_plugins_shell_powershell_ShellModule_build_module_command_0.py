
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.shell.powershell import ShellModule

class TestShellModule:
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.shell_module = ShellModule()
    
    @patch('ansible.executor.powershell.bootstrap_wrapper.ps1', return_value="mocked_script")
    def test_build_module_command_basic(self, mock_bootstrap_wrapper):
        cmd = self.shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="Write-Output 'Hello, World!'")
        assert "mocked_script" in cmd
    
    def test_build_module_command_empty_cmd(self):
        cmd = self.shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="")
        assert "mocked_script" in cmd
    
    @patch('ansible.executor.powershell.bootstrap_wrapper.ps1', return_value="mocked_script")
    def test_build_module_command_non_pipelined_cmd(self, mock_bootstrap_wrapper):
        cmd = self.shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="Write-Output 'Hello, World!'")
        assert "mocked_script" in cmd
    
    @patch('ansible.executor.powershell.bootstrap_wrapper.ps1', return_value="mocked_script")
    def test_build_module_command_binary_module(self, mock_bootstrap_wrapper):
        cmd = self.shell_module.build_module_command(env_string="SomeEnvVar=value", shebang=None, cmd="script.exe arg1 arg2")
        assert "mocked_script" in cmd
    
    @patch('ansible.executor.powershell.bootstrap_wrapper.ps1', return_value="mocked_script")
    def test_build_module_command_with_shebang(self, mock_bootstrap_wrapper):
        cmd = self.shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="Write-Output 'Hello, World!'")
        assert "mocked_script" in cmd
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_______________ TestShellModule.test_build_module_command_basic ________________

thing = <module 'ansible.executor.powershell' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/__init__.py'>
comp = 'bootstrap_wrapper'
import_path = 'ansible.executor.powershell.bootstrap_wrapper'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'ansible.executor.powershell' has no attribute 'bootstrap_wrapper'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1248: AttributeError

During handling of the above exception, another exception occurred:

args = (<test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.TestShellModule object at 0x7ffad7590400>,)
keywargs = {}

    @wraps(func)
    def patched(*args, **keywargs):
>       with self.decoration_helper(patched,
                                    args,
                                    keywargs) as (newargs, newkeywargs):

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1376: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:135: in __enter__
    return next(self.gen)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1358: in decoration_helper
    arg = exit_stack.enter_context(patching)
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:492: in enter_context
    result = _cm_type.__enter__(cm)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1431: in __enter__
    self.target = self.getter()
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1618: in <lambda>
    getter = lambda: _importer(target)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1261: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'ansible.executor.powershell' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/__init__.py'>
comp = 'bootstrap_wrapper'
import_path = 'ansible.executor.powershell.bootstrap_wrapper'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'ansible.executor.powershell.bootstrap_wrapper'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1250: ModuleNotFoundError
_____________ TestShellModule.test_build_module_command_empty_cmd ______________

self = <test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.TestShellModule object at 0x7ffad7593520>

    def test_build_module_command_empty_cmd(self):
        cmd = self.shell_module.build_module_command(env_string="SomeEnvVar=value", shebang="#!powershell", cmd="")
>       assert "mocked_script" in cmd
E       AssertionError: assert 'mocked_script' in 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -EncodedCommand JgBjAGgAYwBwAC4AYwBvAG0AIAA2ADUAM...BjAGsAXQA6ADoAQwByAGUAYQB0AGUAKAAkAHMAcABsAGkAdABfAHAAYQByAHQAcwBbADAAXQApAAoAJgAkAGUAeABlAGMAXwB3AHIAYQBwAHAAZQByAA=='

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py:19: AssertionError
_________ TestShellModule.test_build_module_command_non_pipelined_cmd __________

thing = <module 'ansible.executor.powershell' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/__init__.py'>
comp = 'bootstrap_wrapper'
import_path = 'ansible.executor.powershell.bootstrap_wrapper'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'ansible.executor.powershell' has no attribute 'bootstrap_wrapper'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1248: AttributeError

During handling of the above exception, another exception occurred:

args = (<test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.TestShellModule object at 0x7ffad7593700>,)
keywargs = {}

    @wraps(func)
    def patched(*args, **keywargs):
>       with self.decoration_helper(patched,
                                    args,
                                    keywargs) as (newargs, newkeywargs):

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1376: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:135: in __enter__
    return next(self.gen)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1358: in decoration_helper
    arg = exit_stack.enter_context(patching)
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:492: in enter_context
    result = _cm_type.__enter__(cm)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1431: in __enter__
    self.target = self.getter()
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1618: in <lambda>
    getter = lambda: _importer(target)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1261: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'ansible.executor.powershell' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/__init__.py'>
comp = 'bootstrap_wrapper'
import_path = 'ansible.executor.powershell.bootstrap_wrapper'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'ansible.executor.powershell.bootstrap_wrapper'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1250: ModuleNotFoundError
___________ TestShellModule.test_build_module_command_binary_module ____________

thing = <module 'ansible.executor.powershell' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/__init__.py'>
comp = 'bootstrap_wrapper'
import_path = 'ansible.executor.powershell.bootstrap_wrapper'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'ansible.executor.powershell' has no attribute 'bootstrap_wrapper'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1248: AttributeError

During handling of the above exception, another exception occurred:

args = (<test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.TestShellModule object at 0x7ffad7593880>,)
keywargs = {}

    @wraps(func)
    def patched(*args, **keywargs):
>       with self.decoration_helper(patched,
                                    args,
                                    keywargs) as (newargs, newkeywargs):

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1376: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:135: in __enter__
    return next(self.gen)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1358: in decoration_helper
    arg = exit_stack.enter_context(patching)
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:492: in enter_context
    result = _cm_type.__enter__(cm)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1431: in __enter__
    self.target = self.getter()
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1618: in <lambda>
    getter = lambda: _importer(target)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1261: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'ansible.executor.powershell' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/__init__.py'>
comp = 'bootstrap_wrapper'
import_path = 'ansible.executor.powershell.bootstrap_wrapper'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'ansible.executor.powershell.bootstrap_wrapper'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1250: ModuleNotFoundError
____________ TestShellModule.test_build_module_command_with_shebang ____________

thing = <module 'ansible.executor.powershell' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/__init__.py'>
comp = 'bootstrap_wrapper'
import_path = 'ansible.executor.powershell.bootstrap_wrapper'

    def _dot_lookup(thing, comp, import_path):
        try:
>           return getattr(thing, comp)
E           AttributeError: module 'ansible.executor.powershell' has no attribute 'bootstrap_wrapper'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1248: AttributeError

During handling of the above exception, another exception occurred:

args = (<test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.TestShellModule object at 0x7ffad7593a00>,)
keywargs = {}

    @wraps(func)
    def patched(*args, **keywargs):
>       with self.decoration_helper(patched,
                                    args,
                                    keywargs) as (newargs, newkeywargs):

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1376: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:135: in __enter__
    return next(self.gen)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1358: in decoration_helper
    arg = exit_stack.enter_context(patching)
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:492: in enter_context
    result = _cm_type.__enter__(cm)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1431: in __enter__
    self.target = self.getter()
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1618: in <lambda>
    getter = lambda: _importer(target)
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1261: in _importer
    thing = _dot_lookup(thing, comp, import_path)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

thing = <module 'ansible.executor.powershell' from '/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/__init__.py'>
comp = 'bootstrap_wrapper'
import_path = 'ansible.executor.powershell.bootstrap_wrapper'

    def _dot_lookup(thing, comp, import_path):
        try:
            return getattr(thing, comp)
        except AttributeError:
>           __import__(import_path)
E           ModuleNotFoundError: No module named 'ansible.executor.powershell.bootstrap_wrapper'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1250: ModuleNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py::TestShellModule::test_build_module_command_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py::TestShellModule::test_build_module_command_empty_cmd
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py::TestShellModule::test_build_module_command_non_pipelined_cmd
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py::TestShellModule::test_build_module_command_binary_module
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_shell_powershell_ShellModule_build_module_command_0.py::TestShellModule::test_build_module_command_with_shebang
============================== 5 failed in 0.83s ===============================
"""