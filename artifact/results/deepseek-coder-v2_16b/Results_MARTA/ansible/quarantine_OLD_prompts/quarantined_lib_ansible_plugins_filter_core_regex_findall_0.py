
import pytest
from unittest.mock import patch
from ansible.plugins.filter.core import regex_findall, to_text
import re


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_regex_findall_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        value, regex = 'hello world', 'o'
        with patch('ansible.plugins.filter.core.to_text', return_value="hello world"):
            result = regex_findall(value, regex)
>           assert result == ['o']
E           AssertionError: assert ['o', 'o'] == ['o']
E             
E             Left contains one more item: 'o'
E             Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_regex_findall_0.py:11: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        value, regex = 12345, '\\d'
        with patch('ansible.plugins.filter.core.to_text', return_value="12345"):
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_regex_findall_0.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_regex_findall_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_regex_findall_0.py::test_invalid_input
============================== 2 failed in 0.52s ===============================
"""