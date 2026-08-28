
import pytest
from ansible.module_utils.urls import rfc2822_date_string


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_rfc2822_date_string_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        timetuple = (2001, 11, 9, 1, 8, 7, 4)
        expected_output = 'Fri, 09 Nov 2001 01:08:47 -0000'
>       assert rfc2822_date_string(timetuple) == expected_output
E       AssertionError: assert 'Fri, 09 Nov ...1:08:07 -0000' == 'Fri, 09 Nov ...1:08:47 -0000'
E         
E         - Fri, 09 Nov 2001 01:08:47 -0000
E         ?                        ^
E         + Fri, 09 Nov 2001 01:08:07 -0000
E         ?                        ^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_rfc2822_date_string_0.py:8: AssertionError
__________________________ test_valid_input_with_zone __________________________

    def test_valid_input_with_zone():
        timetuple = (2001, 11, 9, 1, 8, 7, 4)
        expected_output = 'Fri, 09 Nov 2001 01:08:47 +0530'
>       assert rfc2822_date_string(timetuple, zone='+0530') == expected_output
E       AssertionError: assert 'Fri, 09 Nov ...1:08:07 +0530' == 'Fri, 09 Nov ...1:08:47 +0530'
E         
E         - Fri, 09 Nov 2001 01:08:47 +0530
E         ?                        ^
E         + Fri, 09 Nov 2001 01:08:07 +0530
E         ?                        ^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_rfc2822_date_string_0.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_rfc2822_date_string_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_rfc2822_date_string_0.py::test_valid_input_with_zone
============================== 2 failed in 0.40s ===============================
"""