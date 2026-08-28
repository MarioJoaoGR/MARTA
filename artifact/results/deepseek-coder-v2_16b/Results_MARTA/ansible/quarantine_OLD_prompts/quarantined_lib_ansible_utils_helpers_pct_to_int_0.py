
import pytest
from ansible.utils.helpers import pct_to_int


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
>       assert pct_to_int(50, 200) == 100
E       assert 50 == 100
E        +  where 50 = pct_to_int(50, 200)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_0.py:6: AssertionError
_____________________________ test_with_min_value ______________________________

    def test_with_min_value():
>       assert pct_to_int(15, 100, min_value=5) == 5
E       assert 15 == 5
E        +  where 15 = pct_to_int(15, 100, min_value=5)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_0.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_0.py::test_with_min_value
============================== 2 failed in 0.32s ===============================
"""