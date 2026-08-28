
import pytest
from ansible.errors import AnsibleFilterError
import time

def strftime(string_format, second=None):
    ''' return a date string using string. See https://docs.python.org/3/library/time.html#time.strftime for format '''
    if second is not None:
        try:
            second = float(second)
        except Exception:
            raise AnsibleFilterError('Invalid value for epoch value (%s)' % second)
    return time.strftime(string_format, time.localtime(second))


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_strftime_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        result = strftime('%Y-%m-%d %H:%M:%S', 1680579296.0)
>       assert result == '2023-04-01 12:34:56'
E       AssertionError: assert '2023-04-04 04:34:56' == '2023-04-01 12:34:56'
E         
E         - 2023-04-01 12:34:56
E         ?          ^^^^
E         + 2023-04-04 04:34:56
E         ?          ^^^^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_strftime_0.py:17: AssertionError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
>       with pytest.raises(AnsibleFilterError):
E       Failed: DID NOT RAISE <class 'ansible.errors.AnsibleFilterError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_strftime_0.py:20: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_strftime_0.py::test_valid_input_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_strftime_0.py::test_edge_case_none
============================== 2 failed in 0.28s ===============================
"""