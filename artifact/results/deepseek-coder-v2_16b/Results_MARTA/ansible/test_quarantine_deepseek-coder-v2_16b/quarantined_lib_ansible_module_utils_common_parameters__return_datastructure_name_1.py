
import pytest
from ansible.module_utils.common.parameters import _return_datastructure_name


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__return_datastructure_name_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_case_dict _____________________________

    def test_valid_case_dict():
        obj = {'sensitive': 'data', 'otherkey': 123}
        expected_output = ['data', 'otherkey']
        result = list(_return_datastructure_name(obj))
>       assert result == expected_output, f"Expected {expected_output}, but got {result}"
E       AssertionError: Expected ['data', 'otherkey'], but got ['data', '123']
E       assert ['data', '123'] == ['data', 'otherkey']
E         
E         At index 1 diff: '123' != 'otherkey'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__return_datastructure_name_1.py:9: AssertionError
_____________________________ test_error_case_none _____________________________

    def test_error_case_none():
        obj = None
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__return_datastructure_name_1.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__return_datastructure_name_1.py::test_valid_case_dict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_parameters__return_datastructure_name_1.py::test_error_case_none
============================== 2 failed in 0.66s ===============================
"""