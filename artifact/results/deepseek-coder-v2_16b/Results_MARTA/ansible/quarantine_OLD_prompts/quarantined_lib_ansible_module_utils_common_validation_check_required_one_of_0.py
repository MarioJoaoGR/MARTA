
import pytest
from ansible.module_utils.common.validation import check_required_one_of


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        terms = [["missing1", "missing2"], ["foo", "bar"]]
        parameters = {"param1": 1, "param2": 2, "foo": 3, "bar": 4}
        with pytest.raises(TypeError) as excinfo:
            check_required_one_of(terms, parameters)
>       assert str(excinfo.value) == 'one of the following is required: missing1, missing2 found in terms -> options_context'
E       AssertionError: assert 'one of the f...ng1, missing2' == 'one of the f...tions_context'
E         
E         Skipping 41 identical leading characters in diff, use -v to show
E         - 1, missing2 found in terms -> options_context
E         + 1, missing2

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py:10: AssertionError
______________________________ test_no_error_case ______________________________

    def test_no_error_case():
        terms = [["missing1", "missing2"], ["foo", "bar"]]
        parameters = {"param1": 1, "param2": 2, "foo": 3, "bar": 4}
        with pytest.raises(TypeError) as excinfo:
            check_required_one_of(terms, parameters)
>       assert str(excinfo.value) == 'one of the following is required: missing1, missing2 found in terms -> options_context'
E       AssertionError: assert 'one of the f...ng1, missing2' == 'one of the f...tions_context'
E         
E         Skipping 41 identical leading characters in diff, use -v to show
E         - 1, missing2 found in terms -> options_context
E         + 1, missing2

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py::test_error_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py::test_no_error_case
============================== 2 failed in 0.26s ===============================
"""