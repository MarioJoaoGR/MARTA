
import pytest
from ansible.module_utils.common.parameters import _validate_argument_values, AnsibleValidationErrorMultiple, ArgumentValueError, ArgumentTypeError



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_values_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_parameter ____________________________

    def test_invalid_parameter():
        argument_spec = {'param1': {'type': 'str', 'choices': ['val1', 'val2']}, 'param2': {'type': 'int'}}
        parameters = {'param1': 'invalid_value', 'param2': 5}
        errors = AnsibleValidationErrorMultiple()
    
        _validate_argument_values(argument_spec, parameters, errors=errors)
        assert len(errors.messages) == 1, "Expected one error message but found: {}".format(errors.messages)
>       assert isinstance(errors.messages[0], ArgumentValueError), "Error is not of type ArgumentValueError"
E       AssertionError: Error is not of type ArgumentValueError
E       assert False
E        +  where False = isinstance('value of param1 must be one of: val1, val2, got: invalid_value', ArgumentValueError)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_values_1.py:12: AssertionError
____________________________ test_missing_parameter ____________________________

    def test_missing_parameter():
        argument_spec = {'param1': {'type': 'str', 'choices': ['val1', 'val2']}, 'param2': {'type': 'int'}}
        parameters = {'param2': 5}
        errors = AnsibleValidationErrorMultiple()
    
        _validate_argument_values(argument_spec, parameters, errors=errors)
>       assert len(errors.messages) == 1, "Expected one error message but found: {}".format(errors.messages)
E       AssertionError: Expected one error message but found: []
E       assert 0 == 1
E        +  where 0 = len([])
E        +    where [] = AnsibleValidationErrorMultiple().messages

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_values_1.py:20: AssertionError
_____________________________ test_invalid_choice ______________________________

    def test_invalid_choice():
        argument_spec = {'param1': {'type': 'str', 'choices': ['val1', 'val2']}, 'param2': {'type': 'int'}}
        parameters = {'param1': 'val3', 'param2': 5}
        errors = AnsibleValidationErrorMultiple()
    
        _validate_argument_values(argument_spec, parameters, errors=errors)
        assert len(errors.messages) == 1, "Expected one error message but found: {}".format(errors.messages)
>       assert isinstance(errors.messages[0], ArgumentValueError), "Error is not of type ArgumentValueError"
E       AssertionError: Error is not of type ArgumentValueError
E       assert False
E        +  where False = isinstance('value of param1 must be one of: val1, val2, got: val3', ArgumentValueError)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_values_1.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_values_1.py::test_invalid_parameter
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_values_1.py::test_missing_parameter
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__validate_argument_values_1.py::test_invalid_choice
============================== 3 failed in 0.31s ===============================
"""