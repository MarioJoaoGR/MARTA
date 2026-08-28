
import pytest
from ansible.cli.arguments.option_helpers import version
import sys
import ansible
import j2_version
import C
import HAS_LIBYAML

def test_version_default():
    expected = f"Ansible [core {ansible.__version__}]"
    if _gitinfo():
        expected += " " + _gitinfo()
    expected += f"\n  config file = {C.CONFIG_FILE}"
    expected += f"\n  configured module search path = Default w/o overrides"
    expected += f"\n  ansible python module location = {' '.join(ansible.__path__)}"
    expected += f"\n  ansible collection location = {' '.join(C.COLLECTIONS_PATHS)}"
    expected += f"\n  executable location = {sys.argv[0]}"
    expected += f"\n  python version = {''.join(sys.version.splitlines())}"
    expected += f"\n  jinja version = {j2_version}"
    expected += f"\n  libyaml = {HAS_LIBYAML}"
    
    assert version() == expected

def test_version_with_program():
    program = "custom_prog"
    expected = f"{program} [core {ansible.__version__}]"
    if _gitinfo():
        expected += " " + _gitinfo()
    expected += f"\n  config file = {C.CONFIG_FILE}"
    expected += f"\n  configured module search path = Default w/o overrides"
    expected += f"\n  ansible python module location = {' '.join(ansible.__path__)}"
    expected += f"\n  ansible collection location = {' '.join(C.COLLECTIONS_PATHS)}"
    expected += f"\n  executable location = {sys.argv[0]}"
    expected += f"\n  python version = {''.join(sys.version.splitlines())}"
    expected += f"\n  jinja version = {j2_version}"
    expected += f"\n  libyaml = {HAS_LIBYAML}"
    
    assert version("custom_prog") == expected

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
_ ERROR collecting test_lib_ansible_cli_arguments_option_helpers_version_1.py __
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_version_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_version_1.py:6: in <module>
    import j2_version
E   ModuleNotFoundError: No module named 'j2_version'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_version_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 1.05s ===============================
"""