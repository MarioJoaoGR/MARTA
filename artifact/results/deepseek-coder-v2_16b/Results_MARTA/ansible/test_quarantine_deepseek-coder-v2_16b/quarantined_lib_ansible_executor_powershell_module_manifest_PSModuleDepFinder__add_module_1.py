
import pytest
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
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__add_module_1.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        finder = PSModuleDepFinder()
        name = "NonExistentModule"
        ext = ".psm1"
        fqn = "NonExistentModule"
        optional = True
    
        with pytest.raises(AnsibleError):
>           finder._add_module(name, ext, fqn, optional)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__add_module_1.py:14: 
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__add_module_1.py::test_invalid_input
============================== 1 failed in 0.32s ===============================
"""