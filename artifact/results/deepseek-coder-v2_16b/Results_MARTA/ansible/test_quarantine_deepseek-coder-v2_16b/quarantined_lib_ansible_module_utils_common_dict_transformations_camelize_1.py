
import pytest
from ansible.module_utils.common.dict_transformations import camelize

def test_camelize_basic():
    assert camelize({'some_key': 'value'}) == {'someKey': 'value'}

def test_camelize_list():
    assert camelize([{'another_key': 'example'}, {'yet_another_key': 'test'}]) == [{'anotherKey': 'example'}, {'yetAnotherKey': 'test'}]

def test_camelize_non_dict_or_list():
    assert camelize('not_a_dict_or_list') == 'not_a_dict_or_list'

def test_camelize_capitalize_first():
    assert camelize({'some_key': 'value'}, capitalize_first=True) == {'SomeKey': 'value'}

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
_ ERROR collecting test_lib_ansible_module_utils_common_dict_transformations_camelize_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camelize_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camelize_1.py:3: in <module>
    from ansible.module_utils.common.dict_transformations import camelize
E   ImportError: cannot import name 'camelize' from 'ansible.module_utils.common.dict_transformations' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/common/dict_transformations.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_camelize_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.73s ===============================
"""