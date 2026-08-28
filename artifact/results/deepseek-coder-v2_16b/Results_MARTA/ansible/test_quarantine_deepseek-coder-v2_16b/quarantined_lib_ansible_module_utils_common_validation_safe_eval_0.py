
import pytest
from ansible.module_utils.common.validation import safe_eval


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_safe_eval_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________ test_safe_eval_method_call_not_allowed ____________________

    def test_safe_eval_method_call_not_allowed():
        value = "os.path.join('foo', 'bar')"
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_safe_eval_0.py:7: Failed
_________________ test_safe_eval_import_statement_not_allowed __________________

    def test_safe_eval_import_statement_not_allowed():
        value = "import os"
>       with pytest.raises(ImportError):
E       Failed: DID NOT RAISE <class 'ImportError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_safe_eval_0.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_safe_eval_0.py::test_safe_eval_method_call_not_allowed
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_safe_eval_0.py::test_safe_eval_import_statement_not_allowed
============================== 2 failed in 0.25s ===============================
"""