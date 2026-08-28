
import pytest
from ansible.module_utils.common.dict_transformations import _snake_to_camel

# Test cases for default snake to camel conversion without capitalization
@pytest.mark.parametrize("test_data", [('this_is_a_test', False), ('another_example', False)])
def test_valid_case_default(test_data):
    snake, _ = test_data
    assert _snake_to_camel(snake) == 'ThisIsATest'

# Test cases for snake to camel conversion with capitalization of the first letter
@pytest.mark.parametrize("test_data", [('this_is_a_test', True), ('another_example', False)])
def test_valid_case_capitalize_first(test_data):
    snake, capitalize_first = test_data
    if capitalize_first:
        assert _snake_to_camel(snake, capitalize_first=True) == 'This_is_a_test'
    else:
        assert _snake_to_camel(snake) == 'ThisIsATest'
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__snake_to_camel_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_____________________ test_valid_case_default[test_data0] ______________________

test_data = ('this_is_a_test', False)

    @pytest.mark.parametrize("test_data", [('this_is_a_test', False), ('another_example', False)])
    def test_valid_case_default(test_data):
        snake, _ = test_data
>       assert _snake_to_camel(snake) == 'ThisIsATest'
E       AssertionError: assert 'thisIsATest' == 'ThisIsATest'
E         
E         - ThisIsATest
E         ? ^
E         + thisIsATest
E         ? ^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__snake_to_camel_0.py:9: AssertionError
_____________________ test_valid_case_default[test_data1] ______________________

test_data = ('another_example', False)

    @pytest.mark.parametrize("test_data", [('this_is_a_test', False), ('another_example', False)])
    def test_valid_case_default(test_data):
        snake, _ = test_data
>       assert _snake_to_camel(snake) == 'ThisIsATest'
E       AssertionError: assert 'anotherExample' == 'ThisIsATest'
E         
E         - ThisIsATest
E         + anotherExample

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__snake_to_camel_0.py:9: AssertionError
_________________ test_valid_case_capitalize_first[test_data0] _________________

test_data = ('this_is_a_test', True)

    @pytest.mark.parametrize("test_data", [('this_is_a_test', True), ('another_example', False)])
    def test_valid_case_capitalize_first(test_data):
        snake, capitalize_first = test_data
        if capitalize_first:
>           assert _snake_to_camel(snake, capitalize_first=True) == 'This_is_a_test'
E           AssertionError: assert 'ThisIsATest' == 'This_is_a_test'
E             
E             - This_is_a_test
E             + ThisIsATest

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__snake_to_camel_0.py:16: AssertionError
_________________ test_valid_case_capitalize_first[test_data1] _________________

test_data = ('another_example', False)

    @pytest.mark.parametrize("test_data", [('this_is_a_test', True), ('another_example', False)])
    def test_valid_case_capitalize_first(test_data):
        snake, capitalize_first = test_data
        if capitalize_first:
            assert _snake_to_camel(snake, capitalize_first=True) == 'This_is_a_test'
        else:
>           assert _snake_to_camel(snake) == 'ThisIsATest'
E           AssertionError: assert 'anotherExample' == 'ThisIsATest'
E             
E             - ThisIsATest
E             + anotherExample

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__snake_to_camel_0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__snake_to_camel_0.py::test_valid_case_default[test_data0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__snake_to_camel_0.py::test_valid_case_default[test_data1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__snake_to_camel_0.py::test_valid_case_capitalize_first[test_data0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_dict_transformations__snake_to_camel_0.py::test_valid_case_capitalize_first[test_data1]
============================== 4 failed in 0.29s ===============================
"""