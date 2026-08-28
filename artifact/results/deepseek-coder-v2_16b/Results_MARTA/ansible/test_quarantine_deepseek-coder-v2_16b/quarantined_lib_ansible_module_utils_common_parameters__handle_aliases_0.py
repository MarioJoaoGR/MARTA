
import pytest
from ansible.module_utils.common.parameters import _handle_aliases


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__handle_aliases_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        argument_spec = {
            'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
            'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
        }
        parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
        alias_warnings = []
        alias_deprecations = []
    
        result = _handle_aliases(argument_spec, parameters, alias_warnings, alias_deprecations)
    
        assert parameters['option1'] == 'value2'
        assert parameters['option2'] == 'value3'
>       assert not alias_warnings
E       AssertionError: assert not [('option1', 'alias2')]

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__handle_aliases_0.py:18: AssertionError
_______________________________ test_error_case ________________________________

    def test_error_case():
        argument_spec = {
            'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
            'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
        }
        parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
        alias_warnings = []
        alias_deprecations = []
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__handle_aliases_0.py:29: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__handle_aliases_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__handle_aliases_0.py::test_error_case
============================== 2 failed in 0.31s ===============================
"""