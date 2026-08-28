
import pytest
from ansible.module_utils.common.parameters import remove_values




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_remove_values_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________________ test_valid_input_string ____________________________

    def test_valid_input_string():
        result = remove_values("hello world", {"world"})
>       assert result == "hello *"
E       AssertionError: assert 'hello ********' == 'hello *'
E         
E         - hello *
E         + hello ********

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_remove_values_1.py:7: AssertionError
____________________________ test_valid_input_dict _____________________________

    def test_valid_input_dict():
        result = remove_values({"username": "admin", "password": "secret"}, {"admin", "secret"})
>       assert result == {'username': '*', 'password': '*'}
E       AssertionError: assert {'password': ...OG_PARAMETER'} == {'password': ...sername': '*'}
E         
E         Differing items:
E         {'password': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'} != {'password': '*'}
E         {'username': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'} != {'username': '*'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_remove_values_1.py:11: AssertionError
____________________________ test_valid_input_list _____________________________

    def test_valid_input_list():
        result = remove_values([1, 2, 3], {2})
>       assert result == [1, 3]
E       AssertionError: assert [1, 'VALUE_SP...PARAMETER', 3] == [1, 3]
E         
E         At index 1 diff: 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER' != 3
E         Left contains one more item: 3
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_remove_values_1.py:15: AssertionError
__________________________ test_nested_container_dict __________________________

    def test_nested_container_dict():
        data = {"level1": {"level2": {"sensitive_key": "sensitive_value"}}}
        result = remove_values(data, {"sensitive_value"})
>       assert result == {'level1': {'level2': {}}}
E       AssertionError: assert {'level1': {'..._PARAMETER'}}} == {'level1': {'level2': {}}}
E         
E         Differing items:
E         {'level1': {'level2': {'sensitive_key': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'}}} != {'level1': {'level2': {}}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_remove_values_1.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_remove_values_1.py::test_valid_input_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_remove_values_1.py::test_valid_input_dict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_remove_values_1.py::test_valid_input_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_remove_values_1.py::test_nested_container_dict
============================== 4 failed in 0.66s ===============================
"""