
import pytest
from ansible.module_utils.common.parameters import _validate_argument_types
from ansible.errors import ArgumentTypeError, AnsibleValidationErrorMultiple

def test_validate_integer_parameter():
    argument_spec = {'param1': {'type': 'int'}}
    parameters = {'param1': 1}
    validated_params, errors = _validate_argument_types(argument_spec, parameters)
    assert validated_params == {'param1': 1}
    assert len(errors) == 0

def test_validate_string_parameter():
    argument_spec = {'param2': {'type': 'str'}}
    parameters = {'param2': 'string'}
    validated_params, errors = _validate_argument_types(argument_spec, parameters)
    assert validated_params == {'param2': 'string'}
    assert len(errors) == 0

def test_validate_list_of_integers():
    argument_spec = {'param1': {'type': 'list', 'elements': 'int'}}
    parameters = {'param1': [1, 2, 3]}
    validated_params, errors = _validate_argument_types(argument_spec, parameters)
    assert validated_params == {'param1': [1, 2, 3]}
    assert len(errors) == 0

def test_invalid_element_in_list():
    argument_spec = {'param1': {'type': 'list', 'elements': 'int'}}
    parameters = {'param1': [1, 'string', 3.14]}
    validated_params, errors = _validate_argument_types(argument_spec, parameters)
    assert len(validated_params) == 0
    assert len(errors) == 1
    assert isinstance(errors[0], ArgumentTypeError)
    assert "Invalid type <class 'str'> for option 'param1'" in str(errors[0])

def test_validate_nested_options():
    argument_spec = {'param1': {'type': 'int'}, 'nested_option': {'type': 'str'}}
    parameters = {'nested_option': {'param1': 1}}
    options_context = ['nested_option']
    validated_params, errors = _validate_argument_types(argument_spec, parameters, options_context=options_context)
    assert len(validated_params) == 0
    assert len(errors) == 1
    assert isinstance(errors[0], ArgumentTypeError)
    assert "Invalid type <class 'int'> for option 'param1'" in str(errors[0])

def test_custom_error_handling():
    argument_spec = {'custom_error': {'type': 'int'}}
    parameters = {'custom_error': 1}
    errors = AnsibleValidationErrorMultiple()
    validated_params, errors = _validate_argument_types(argument_spec, parameters, errors=errors)
    assert validated_params == {'custom_error': 1}
    assert len(errors) == 0

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
_ ERROR collecting test_lib_ansible_module_utils_common_parameters__validate_argument_types_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_types_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_types_0.py:4: in <module>
    from ansible.errors import ArgumentTypeError, AnsibleValidationErrorMultiple
E   ImportError: cannot import name 'ArgumentTypeError' from 'ansible.errors' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/errors/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_types_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.37s ===============================
"""