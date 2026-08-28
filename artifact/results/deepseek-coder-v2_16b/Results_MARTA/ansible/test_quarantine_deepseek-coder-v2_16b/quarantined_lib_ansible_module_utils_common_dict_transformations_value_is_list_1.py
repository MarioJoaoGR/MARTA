
import pytest
from ansible.module_utils.common.dict_transformations import camel_to_snake

def value_is_list(camel_list):
    """
    Recursively processes a list to convert dictionary keys from camelCase to snake_case and handles nested lists.
    
    Parameters:
        camel_list (list): A list containing dictionaries with camelCase keys, other lists, or other types.
        
    Returns:
        list: A new list where the dictionary keys are converted from camelCase to snake_case, and nested lists are processed recursively.
    """
    checked_list = []
    for item in camel_list:
        if isinstance(item, dict):
            new_dict = {}
            for key, value in item.items():
                new_key = camel_to_snake(key)
                if isinstance(value, list):
                    new_dict[new_key] = value_is_list(value)
                else:
                    new_dict[new_key] = value
            checked_list.append(new_dict)
        elif isinstance(item, list):
            checked_list.append(value_is_list(item))
        else:
            checked_list.append(item)
    return checked_list

# Test cases for the value_is_list function
def test_value_is_list_basic():
    example_input = [{'camelCaseKey': 123, 'anotherKey': [456, {'moreCamelCase': 789}]}]
    expected_output = [{'snake_case_key': 123, 'another_key': [456, {'more_camel_case': 789}]}]
    assert value_is_list(example_input) == expected_output

def test_value_is_list_nested():
    nested_input = [[{'camelCaseKey': 123}, [456, [{'moreCamelCase': 789}]]], 'string']
    expected_output = [[{'snake_case_key': 123}, [456, [{'more_camel_case': 789}]]], 'string']
    assert value_is_list(nested_input) == expected_output

def test_value_is_list_empty():
    empty_input = []
    expected_output = []
    assert value_is_list(empty_input) == expected_output

def test_value_is_list_mixed():
    mixed_input = [1, 'string', {'camelCaseKey': 123}, [456, [{'moreCamelCase': 789}]]]
    expected_output = [1, 'string', {'snake_case_key': 123}, [456, [{'more_camel_case': 789}]]]
    assert value_is_list(mixed_input) == expected_output

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
_ ERROR collecting test_lib_ansible_module_utils_common_dict_transformations_value_is_list_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_value_is_list_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_value_is_list_1.py:3: in <module>
    from ansible.module_utils.common.dict_transformations import camel_to_snake
E   ImportError: cannot import name 'camel_to_snake' from 'ansible.module_utils.common.dict_transformations' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/common/dict_transformations.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations_value_is_list_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.74s ===============================
"""