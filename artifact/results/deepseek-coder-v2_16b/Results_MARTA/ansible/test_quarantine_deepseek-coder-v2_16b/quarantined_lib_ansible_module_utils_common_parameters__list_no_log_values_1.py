
import pytest
from ansible.module_utils.common.parameters import _list_no_log_values


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__list_no_log_values_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        arg_spec = {
            'username': {'type': 'str', 'no_log': True},
            'password': {'options': {'secret': {'type': 'str', 'no_log': True}}}
        }
        params = {
            'username': 'admin',
            'password': {'secret': 'supersecret'}
        }
        no_log_values = _list_no_log_values(arg_spec, params)
>       assert no_log_values == {'admin', 'supersecret'}
E       AssertionError: assert {'admin'} == {'admin', 'supersecret'}
E         
E         Extra items in the right set:
E         'supersecret'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__list_no_log_values_1.py:15: AssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        arg_spec = {
            'users': {'type': 'list', 'elements': 'dict', 'options': {
                'name': {'type': 'str'},
                'password': {'type': 'str', 'no_log': True}
            }}
        }
        params = {'users': [{'name': 'user1', 'password': 'pass1'}, {'name': 'user2'}]}
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__list_no_log_values_1.py:25: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__list_no_log_values_1.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__list_no_log_values_1.py::test_invalid_inputs
============================== 2 failed in 0.67s ===============================
"""