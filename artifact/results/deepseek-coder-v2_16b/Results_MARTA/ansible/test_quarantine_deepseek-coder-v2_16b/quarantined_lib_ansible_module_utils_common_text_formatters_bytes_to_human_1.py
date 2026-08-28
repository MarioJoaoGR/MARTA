
import pytest
from ansible.module_utils.common.text.formatters import bytes_to_human



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_bytes_to_human_isbits __________________________

    def test_bytes_to_human_isbits():
>       assert bytes_to_human(1024, isbits=True) == '8.00 Kb'
E       AssertionError: assert '1.00 Kb' == '8.00 Kb'
E         
E         - 8.00 Kb
E         ? ^
E         + 1.00 Kb
E         ? ^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_1.py:6: AssertionError
______________________ test_bytes_to_human_specified_unit ______________________

    def test_bytes_to_human_specified_unit():
>       assert bytes_to_human(1500, unit='B') == '1.46 KB'
E       AssertionError: assert '1500.00 Bytes' == '1.46 KB'
E         
E         - 1.46 KB
E         + 1500.00 Bytes

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_1.py:9: AssertionError
___________________ test_bytes_to_human_both_isbits_and_unit ___________________

    def test_bytes_to_human_both_isbits_and_unit():
>       assert bytes_to_human(1500, isbits=True, unit='K') == '12.50 Kb'
E       AssertionError: assert '1.46 Kb' == '12.50 Kb'
E         
E         - 12.50 Kb
E         + 1.46 Kb

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_1.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_1.py::test_bytes_to_human_isbits
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_1.py::test_bytes_to_human_specified_unit
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_1.py::test_bytes_to_human_both_isbits_and_unit
============================== 3 failed in 0.65s ===============================
"""