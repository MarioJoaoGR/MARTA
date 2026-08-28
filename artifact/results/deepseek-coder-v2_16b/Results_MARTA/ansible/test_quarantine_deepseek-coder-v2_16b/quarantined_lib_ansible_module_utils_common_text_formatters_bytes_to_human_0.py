
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_specified_unit ________________________

    def test_valid_input_specified_unit():
        result = bytes_to_human(1500, unit='B')
>       assert result == '1.46 KB', f"Expected '1.46 KB' but got '{result}'"
E       AssertionError: Expected '1.46 KB' but got '1500.00 Bytes'
E       assert '1500.00 Bytes' == '1.46 KB'
E         
E         - 1.46 KB
E         + 1500.00 Bytes

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_0.py:7: AssertionError
_____________________ test_valid_input_specified_bits_unit _____________________

    def test_valid_input_specified_bits_unit():
        result = bytes_to_human(1024, isbits=True)
>       assert result == '8.00 Kb', f"Expected '8.00 Kb' but got '{result}'"
E       AssertionError: Expected '8.00 Kb' but got '1.00 Kb'
E       assert '1.00 Kb' == '8.00 Kb'
E         
E         - 8.00 Kb
E         ? ^
E         + 1.00 Kb
E         ? ^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_0.py::test_valid_input_specified_unit
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_formatters_bytes_to_human_0.py::test_valid_input_specified_bits_unit
============================== 2 failed in 0.30s ===============================
"""