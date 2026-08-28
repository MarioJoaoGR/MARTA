
import pytest
import json
from ansible.plugins.filter.core import to_json
from ansible.module_utils.common.jsonclass import AnsibleJSONEncoder

def test_to_json_basic():
    result = to_json({'key': 'value'})
    assert isinstance(result, str), "Expected a JSON string"
    expected_output = json.dumps({'key': 'value'}, cls=AnsibleJSONEncoder)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_to_json_with_indent():
    result = to_json({'key': 'value'}, indent=4)
    assert isinstance(result, str), "Expected a JSON string"
    expected_output = json.dumps({'key': 'value'}, cls=AnsibleJSONEncoder, indent=4)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_to_json_with_sort_keys():
    result = to_json({'b': 2, 'a': 1}, sort_keys=True)
    assert isinstance(result, str), "Expected a JSON string"
    expected_output = json.dumps({'b': 2, 'a': 1}, cls=AnsibleJSONEncoder, sort_keys=True)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_to_json_with_custom_encoder():
    import json
    from ansible.module_utils.common.jsonclass import AnsibleJSONEncoder
    
    result = to_json({'key': 'value'}, cls=AnsibleJSONEncoder)
    assert isinstance(result, str), "Expected a JSON string"
    expected_output = json.dumps({'key': 'value'}, cls=AnsibleJSONEncoder)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_to_json_with_additional_args():
    result = to_json({'key': 'value'}, separators=(',', ':'))
    assert isinstance(result, str), "Expected a JSON string"
    expected_output = json.dumps({'key': 'value'}, cls=AnsibleJSONEncoder, separators=(',', ':'))
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

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
______ ERROR collecting test_lib_ansible_plugins_filter_core_to_json_0.py ______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_json_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_json_0.py:5: in <module>
    from ansible.module_utils.common.jsonclass import AnsibleJSONEncoder
E   ModuleNotFoundError: No module named 'ansible.module_utils.common.jsonclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_json_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.74s ===============================
"""