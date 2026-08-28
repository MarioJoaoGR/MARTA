
import pytest
from ansible.module_utils.common.validation import check_required_together


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_together_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________ test_check_required_together_missing_parameter ________________

    def test_check_required_together_missing_parameter():
        terms = [["param1", "param2"], ["param4"]]
        parameters = {"param1": 1, "param3": 3}
        with pytest.raises(TypeError) as excinfo:
            check_required_together(terms, parameters)
>       assert str(excinfo.value) == 'parameters are required together: param2, param4'
E       AssertionError: assert 'parameters a...aram1, param2' == 'parameters a...aram2, param4'
E         
E         - parameters are required together: param2, param4
E         ?                                         --------
E         + parameters are required together: param1, param2
E         ?                                   ++++++++

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_together_0.py:10: AssertionError
_________________ test_check_required_together_complex_nested __________________

    def test_check_required_together_complex_nested():
        terms = [["paramA", "paramB"], ["paramC", "paramD"]]
        parameters = {"paramA": 1, "paramE": 5}
        with pytest.raises(TypeError) as excinfo:
            check_required_together(terms, parameters)
>       assert str(excinfo.value) == 'parameters are required together: paramB, paramC, paramD'
E       AssertionError: assert 'parameters a...aramA, paramB' == 'parameters a...aramC, paramD'
E         
E         - parameters are required together: paramB, paramC, paramD
E         ?                                         ----------------
E         + parameters are required together: paramA, paramB
E         ?                                   ++++++++

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_together_0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_together_0.py::test_check_required_together_missing_parameter
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_together_0.py::test_check_required_together_complex_nested
============================== 2 failed in 0.31s ===============================
"""