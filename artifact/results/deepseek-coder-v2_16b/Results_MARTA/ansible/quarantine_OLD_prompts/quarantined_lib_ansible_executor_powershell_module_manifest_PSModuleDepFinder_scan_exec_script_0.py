
import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.errors import AnsibleError



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder_scan_exec_script_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________ test_scan_exec_script_should_find_dependencies ________________

    def test_scan_exec_script_should_find_dependencies():
        finder = PSModuleDepFinder()
        with patch("ansible.executor.powershell.module_manifest.pkgutil.get_data", return_value=b"#Requires -Module Ansible.ModuleUtils.SomeUtility"):
>           finder.scan_exec_script("SomeScript")

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder_scan_exec_script_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/module_manifest.py:162: in scan_exec_script
    self.scan_module(b_data, wrapper=True, powershell=True)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/module_manifest.py:140: in scan_module
    self._add_module(*m, wrapper=wrapper)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.executor.powershell.module_manifest.PSModuleDepFinder object at 0x7f432b9b4fd0>
name = 'Ansible.ModuleUtils.SomeUtility', ext = '.psm1', fqn = None
optional = False, wrapper = True

    def _add_module(self, name, ext, fqn, optional, wrapper=False):
        m = to_text(name)
    
        util_fqn = None
    
        if m.startswith("Ansible."):
            # Builtin util, use plugin loader to get the data
            mu_path = ps_module_utils_loader.find_plugin(m, ext)
    
            if not mu_path:
                if optional:
                    return
    
>               raise AnsibleError('Could not find imported module support code '
                                   'for \'%s\'' % m)
E               ansible.errors.AnsibleError: Could not find imported module support code for 'Ansible.ModuleUtils.SomeUtility'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/module_manifest.py:177: AnsibleError
___________________________ test_add_module_utility ____________________________

    def test_add_module_utility():
        finder = PSModuleDepFinder()
        module_data = b"""
        #Requires -Module Ansible.ModuleUtils.SomeUtility
        """
        with patch("ansible.executor.powershell.module_manifest._strip_comments", return_value=b"#Requires -Module Ansible.ModuleUtils.SomeUtility"):
>           finder._add_module("SomeUtility", "psm1", "Ansible.ModuleUtils", optional=False)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder_scan_exec_script_0.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/module_manifest.py:198: in _add_module
    module_util = import_module(n_package_name)
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1047: in _gcd_import
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = '', package = None, level = 0

>   ???
E   ValueError: Empty module name

<frozen importlib._bootstrap>:981: ValueError
______________________ test_manage_os_version_requirement ______________________

    def test_manage_os_version_requirement():
        finder = PSModuleDepFinder()
        os_version_data = b"""
        #ansiblerequires -osversion 6.2
        """
        with patch("ansible.executor.powershell.module_manifest._strip_comments", return_value=b"#ansiblerequires -osversion 6.2"):
>           finder._add_module("os_version", "psm1", "Ansible", optional=False)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder_scan_exec_script_0.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/powershell/module_manifest.py:198: in _add_module
    module_util = import_module(n_package_name)
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1047: in _gcd_import
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = '', package = None, level = 0

>   ???
E   ValueError: Empty module name

<frozen importlib._bootstrap>:981: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder_scan_exec_script_0.py::test_scan_exec_script_should_find_dependencies
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder_scan_exec_script_0.py::test_add_module_utility
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder_scan_exec_script_0.py::test_manage_os_version_requirement
============================== 3 failed in 0.34s ===============================
"""