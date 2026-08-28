
import pytest
from unittest.mock import patch
from ansible.module_utils.common.validation import check_mutually_exclusive

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        with patch('ansible.module_utils.common.validation.check_mutually_exclusive') as mock_check:
            mock_check.side_effect = TypeError("parameters are mutually exclusive: param1|param2 found in []")
    
            terms = ["param1", "param2"]
            parameters = {"param1": 1, "param2": 2}
    
>           with pytest.raises(TypeError) as excinfo:
E           Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py::test_error_case
============================== 1 failed in 0.31s ===============================
"""