
import pytest
from ansible.module_utils.common.parameters import _return_datastructure_name
from collections import Mapping, text_type, binary_type

def test_return_datastructure_name_with_dict():
    obj = {"sensitive": "data", "otherkey": 123}
    result = list(_return_datastructure_name(obj))
    assert result == ['data', 'otherkey']

def test_return_datastructure_name_with_list():
    obj = ["sensitive", "data"]
    result = list(_return_datastructure_name(obj))
    assert result == ['sensitive', 'data']

def test_return_datastructure_name_with_string():
    obj = "sensitive data"
    result = list(_return_datastructure_name(obj))
    assert result == ['sensitive', 'data']

def test_return_datastructure_name_with_integer():
    with pytest.raises(TypeError) as e:
        obj = 123
        list(_return_datastructure_name(obj))
    assert str(e.value) == "Unknown parameter type: <class 'int'>"

def test_return_datastructure_name_with_none():
    with pytest.raises(TypeError) as e:
        obj = None
        list(_return_datastructure_name(obj))
    assert str(e.value) == "Unknown parameter type: <class 'NoneType'>"

def test_return_datastructure_name_with_tuple():
    obj = (1, "data")
    result = list(_return_datastructure_name(obj))
    assert result == ['data']

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
_ ERROR collecting test_lib_ansible_module_utils_common_parameters__return_datastructure_name_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__return_datastructure_name_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__return_datastructure_name_0.py:4: in <module>
    from collections import Mapping, text_type, binary_type
E   ImportError: cannot import name 'Mapping' from 'collections' (/opt/conda/envs/test4py_env/lib/python3.10/collections/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__return_datastructure_name_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.36s ===============================
"""