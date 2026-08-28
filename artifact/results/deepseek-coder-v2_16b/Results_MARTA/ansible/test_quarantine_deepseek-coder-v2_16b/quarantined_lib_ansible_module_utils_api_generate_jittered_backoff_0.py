
import pytest
from ansible.module_utils.api import generate_jittered_backoff
import random

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_generate_jittered_backoff_0.py F [100%]

=================================== FAILURES ===================================
____________________________ test_custom_delay_base ____________________________

    def test_custom_delay_base():
        delay_base = 4
        jittered_backoff = list(generate_jittered_backoff(delay_base=delay_base))
        for i, delay in enumerate(jittered_backoff):
            expected_delay = random.randint(0, min(60, delay_base * 2 ** i))
>           assert delay == expected_delay, f"Expected {expected_delay}, but got {delay}"
E           AssertionError: Expected 2, but got 4
E           assert 4 == 2

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_generate_jittered_backoff_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_api_generate_jittered_backoff_0.py::test_custom_delay_base
============================== 1 failed in 0.25s ===============================
"""