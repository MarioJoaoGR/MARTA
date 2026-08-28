
import pytest
from ansible.module_utils.common.dict_transformations import camel_to_snake

def test_camel_to_snake_basic():
    assert camel_to_snake("CamelCaseName") == "camel_case_name"

def test_camel_to_snake_reversible():
    assert camel_to_snake("AnotherCamelCaseExample", reversible=True) == "another_camel_case_example"

def test_camel_to_snake_pluralized_abbreviations():
    assert camel_to_snake("TargetGroupARNs", reversible=True) == "target_group_ar_ns"

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
_ ERROR collecting test_lib_ansible_module_utils_common_dict_transformations__camel_to_snake_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__camel_to_snake_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__camel_to_snake_1.py:3: in <module>
    from ansible.module_utils.common.dict_transformations import camel_to_snake
E   ImportError: cannot import name 'camel_to_snake' from 'ansible.module_utils.common.dict_transformations' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/common/dict_transformations.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__camel_to_snake_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.37s ===============================
"""