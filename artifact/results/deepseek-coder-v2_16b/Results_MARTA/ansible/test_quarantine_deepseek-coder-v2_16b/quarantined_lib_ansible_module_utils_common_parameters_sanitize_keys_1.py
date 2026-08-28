
import pytest
from ansible.module_utils.common.parameters import sanitize_keys


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_sanitize_keys_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_dictionary __________________________

    def test_valid_input_dictionary():
        obj = {'key1': 'no_log', 'key2': 'loggable'}
        no_log_strings = {'no_log'}
        expected_output = {'key1__': '***', 'key2': 'loggable'}
    
        result = sanitize_keys(obj, no_log_strings)
>       assert result == expected_output, f"Expected {expected_output}, but got {result}"
E       AssertionError: Expected {'key1__': '***', 'key2': 'loggable'}, but got {'key1': 'no_log', 'key2': 'loggable'}
E       assert {'key1': 'no_...': 'loggable'} == {'key1__': '*...': 'loggable'}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 1 more item:
E         {'key1': 'no_log'}
E         Right contains 1 more item:
E         {'key1__': '***'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_sanitize_keys_1.py:11: AssertionError
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        obj = 'not a container'
        no_log_strings = {'no_log'}
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_sanitize_keys_1.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_sanitize_keys_1.py::test_valid_input_dictionary
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters_sanitize_keys_1.py::test_invalid_input_error_handling
============================== 2 failed in 0.66s ===============================
"""