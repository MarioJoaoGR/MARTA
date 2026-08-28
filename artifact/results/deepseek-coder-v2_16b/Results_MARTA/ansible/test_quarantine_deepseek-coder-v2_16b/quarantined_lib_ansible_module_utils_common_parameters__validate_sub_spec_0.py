
import pytest
from ansible.module_utils.common.parameters import _validate_sub_spec
from ansible.errors import AnsibleValidationErrorMultiple, SubParameterTypeError, AliasError, NoLogError, MutuallyExclusiveError, RequiredError

def test_validate_sub_spec_with_valid_parameters():
    argument_spec = {
        'param1': {'type': 'str', 'options': {'secret': {'type': 'str', 'no_log': True}}},
        'param2': {'type': 'list', 'elements': 'dict', 'options': {'username': {'type': 'str'}, 'password': {'type': 'str', 'no_log': True}}}
    }
    parameters = {
        'param1': {'secret': 'supersecret'},
        'param2': [{'username': 'admin', 'password': 'mypassword'}, {'username': 'user', 'password': 'yourpassword'}]
    }
    errors = AnsibleValidationErrorMultiple()
    _validate_sub_spec(argument_spec, parameters, prefix='options.', errors=errors)
    assert not errors.messages

def test_validate_sub_spec_with_invalid_type():
    argument_spec = {
        'param1': {'type': 'str', 'options': {'secret': {'type': 'str', 'no_log': True}}},
        'param2': {'type': 'list', 'elements': 'dict', 'options': {'username': {'type': 'str'}, 'password': {'type': 'str', 'no_log': True}}}
    }
    parameters = {
        'param1': {'secret': 12345},  # Invalid type for param1
        'param2': [{'username': 'admin', 'password': 'mypassword'}, {'username': 'user', 'password': 'yourpassword'}]
    }
    errors = AnsibleValidationErrorMultiple()
    with pytest.raises(SubParameterTypeError):
        _validate_sub_spec(argument_spec, parameters, prefix='options.', errors=errors)
    assert len(errors.messages) == 1

def test_validate_sub_spec_with_missing_required_param():
    argument_spec = {
        'param1': {'type': 'str', 'options': {'secret': {'type': 'str', 'no_log': True}}},
        'param2': {'type': 'list', 'elements': 'dict', 'options': {'username': {'type': 'str'}, 'password': {'type': 'str', 'no_log': True}}}
    }
    parameters = {
        'param1': {'secret': 'supersecret'}  # Missing required param2
    }
    errors = AnsibleValidationErrorMultiple()
    with pytest.raises(RequiredError):
        _validate_sub_spec(argument_spec, parameters, prefix='options.', errors=errors)
    assert len(errors.messages) == 1

def test_validate_sub_spec_with_mutually_exclusive_params():
    argument_spec = {
        'param1': {'type': 'str', 'options': {'secret': {'type': 'str', 'no_log': True}}},
        'param2': {'type': 'list', 'elements': 'dict', 'options': {'username': {'type': 'str'}, 'password': {'type': 'str', 'no_log': True, 'mutually_exclusive': ['username']}}}
    }
    parameters = {
        'param1': {'secret': 'supersecret'},
        'param2': [{'username': 'admin', 'password': 'mypassword'}, {'username': 'user', 'password': 'yourpassword'}]  # Both username and password are set, but they should be mutually exclusive
    }
    errors = AnsibleValidationErrorMultiple()
    with pytest.raises(MutuallyExclusiveError):
        _validate_sub_spec(argument_spec, parameters, prefix='options.', errors=errors)
    assert len(errors.messages) == 1

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
_ ERROR collecting test_lib_ansible_module_utils_common_parameters__validate_sub_spec_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_sub_spec_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_sub_spec_0.py:4: in <module>
    from ansible.errors import AnsibleValidationErrorMultiple, SubParameterTypeError, AliasError, NoLogError, MutuallyExclusiveError, RequiredError
E   ImportError: cannot import name 'AnsibleValidationErrorMultiple' from 'ansible.errors' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/errors/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_sub_spec_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.37s ===============================
"""