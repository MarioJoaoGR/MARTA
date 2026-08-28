
import pytest
from ansible.module_utils.api import retry
import time



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_retry_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_retry_without_retries __________________________

    def test_retry_without_retries():
        @retry(retry_pause=0)
        def risky_function():
            raise Exception("Test exception")
    
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_retry_0.py:11: Failed
___________________________ test_retry_with_retries ____________________________

    def test_retry_with_retries():
        @retry(retries=3, retry_pause=0)
        def risky_function():
            if not hasattr(risky_function, "attempt"):
                setattr(risky_function, "attempt", 0)
            attempt = getattr(risky_function, "attempt")
            if attempt == 2:
                return True
            raise Exception("Test exception")
    
        with pytest.raises(Exception):
            risky_function()
>       assert risky_function.attempt == 3
E       assert 0 == 3
E        +  where 0 = <function retry.<locals>.wrapper.<locals>.retried at 0x7fd479070940>.attempt

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_retry_0.py:26: AssertionError
______________________ test_retry_with_retries_and_pause _______________________

    def test_retry_with_retries_and_pause():
        @retry(retries=2, retry_pause=0.1)
        def risky_function():
            if not hasattr(risky_function, "attempt"):
                setattr(risky_function, "attempt", 0)
            attempt = getattr(risky_function, "attempt")
            if attempt == 2:
                return True
            raise Exception("Test exception")
    
        with pytest.raises(Exception):
            risky_function()
>       assert risky_function.attempt == 3
E       assert 0 == 3
E        +  where 0 = <function retry.<locals>.wrapper.<locals>.retried at 0x7fd47928de10>.attempt

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_retry_0.py:40: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_retry_0.py::test_retry_without_retries
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_retry_0.py::test_retry_with_retries
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_retry_0.py::test_retry_with_retries_and_pause
============================== 3 failed in 0.37s ===============================
"""