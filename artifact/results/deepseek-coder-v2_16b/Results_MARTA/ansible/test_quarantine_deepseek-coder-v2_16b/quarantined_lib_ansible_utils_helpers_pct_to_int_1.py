
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_valid_case_integer_input _________________________

    def test_valid_case_integer_input():
        value = 50
        num_items = 200
        result = pct_to_int(value, num_items)
>       assert result == 100
E       assert 50 == 100

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_1.py:9: AssertionError
_________________________ test_edge_case_minimum_value _________________________

    def test_edge_case_minimum_value():
        value = 15
        num_items = 100
        min_value = 5
        result = pct_to_int(value, num_items, min_value)
>       assert result == 5
E       assert 15 == 5

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_1.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_1.py::test_valid_case_integer_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_helpers_pct_to_int_1.py::test_edge_case_minimum_value
============================== 2 failed in 0.61s ===============================
"""