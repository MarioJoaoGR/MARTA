
import pytest
from ansible.module_utils.common.parameters import _get_legal_inputs


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        argument_spec = {
            'option1': {'aliases': ['alias1', 'alias2'], 'default': None, 'required': False},
            'option2': {'aliases': ['alias3'], 'default': None, 'required': True}
        }
        parameters = {'alias1': 'value1', 'alias2': 'value2', 'alias3': 'value3'}
    
        legal_inputs = _get_legal_inputs(argument_spec, parameters)
>       assert set(legal_inputs) == {'option1', 'option2'}
E       AssertionError: assert {'alias1', 'a...1', 'option2'} == {'option1', 'option2'}
E         
E         Extra items in the left set:
E         'alias3'
E         'alias1'
E         'alias2'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py:13: AssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        argument_spec = {
            'option1': {'default': None, 'required': True},
            'option2': {'aliases': ['alias1'], 'default': None, 'required': False}
        }
        parameters = {}
    
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__get_legal_inputs_0.py::test_invalid_inputs
============================== 2 failed in 0.66s ===============================
"""