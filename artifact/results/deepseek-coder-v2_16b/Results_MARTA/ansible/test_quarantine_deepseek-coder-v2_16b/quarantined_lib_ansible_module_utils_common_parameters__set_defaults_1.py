
import pytest
from ansible.module_utils.common.parameters import _set_defaults



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__set_defaults_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        argument_spec = {
            'param1': {'default': 'value1', 'no_log': False},
            'param2': {'default': None, 'no_log': True}
        }
        parameters = {}
    
        result = _set_defaults(argument_spec, parameters)
    
>       assert parameters == {'param1': 'value1'}
E       AssertionError: assert {'param1': 'v...param2': None} == {'param1': 'value1'}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 1 more item:
E         {'param2': None}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__set_defaults_1.py:14: AssertionError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        argument_spec = {
            'param1': {'default': 'value1', 'no_log': False},
            'param2': {'default': None, 'no_log': True}
        }
        parameters = {}
    
        result = _set_defaults(argument_spec, parameters)
    
>       assert parameters == {'param1': 'value1'}
E       AssertionError: assert {'param1': 'v...param2': None} == {'param1': 'value1'}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 1 more item:
E         {'param2': None}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__set_defaults_1.py:26: AssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        argument_spec = {
            'param1': {'default': 'value1', 'no_log': False},
            'param2': {'default': None, 'no_log': True}
        }
        parameters = {}
    
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__set_defaults_1.py:36: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__set_defaults_1.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__set_defaults_1.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__set_defaults_1.py::test_invalid_inputs
============================== 3 failed in 0.67s ===============================
"""