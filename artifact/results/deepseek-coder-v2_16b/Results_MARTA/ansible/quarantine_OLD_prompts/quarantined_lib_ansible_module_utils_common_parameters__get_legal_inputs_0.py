
import pytest
from ansible.module_utils.common.parameters import _get_legal_inputs, _handle_aliases



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_missing_required_option _________________________

    def test_missing_required_option():
        argument_spec = {
            'option1': {'default': None, 'required': True},
            'option2': {'aliases': ['alias1'], 'default': None, 'required': False}
        }
        parameters = {}
    
>       with pytest.raises(Exception) as e:
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py:12: Failed
_________________________ test_missing_optional_option _________________________

    def test_missing_optional_option():
        argument_spec = {
            'option1': {'default': None, 'required': False},
            'option2': {'aliases': ['alias1'], 'default': None, 'required': True}
        }
        parameters = {}
    
>       with pytest.raises(Exception) as e:
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py:23: Failed
______________________________ test_with_aliases _______________________________

    def test_with_aliases():
        argument_spec = {
            'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
            'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
        }
        parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
    
        legal_inputs = _get_legal_inputs(argument_spec, parameters)
>       assert sorted(legal_inputs) == ['option1', 'option2']
E       AssertionError: assert ['alias1', 'a...1', 'option2'] == ['option1', 'option2']
E         
E         At index 0 diff: 'alias1' != 'option1'
E         Left contains 3 more items, first extra item: 'alias3'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py:35: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py::test_missing_required_option
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py::test_missing_optional_option
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py::test_with_aliases
============================== 3 failed in 0.28s ===============================
"""