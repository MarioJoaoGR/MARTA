
import pytest
import re
from ansible.plugins.filter.core import regex_findall


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
___________________________ test_regex_findall_basic ___________________________

    def test_regex_findall_basic():
        result = regex_findall("hello world", r"o")
>       assert result == ['o']
E       AssertionError: assert ['o', 'o'] == ['o']
E         
E         Left contains one more item: 'o'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_regex_findall_0.py:8: AssertionError
_____________________ test_regex_findall_mixed_parameters ______________________

    def test_regex_findall_mixed_parameters():
        result = regex_findall("Hello World!", r"[a-z]+", ignorecase=True, multiline=False)
>       assert result == ['ello', 'orld']
E       AssertionError: assert ['Hello', 'World'] == ['ello', 'orld']
E         
E         At index 0 diff: 'Hello' != 'ello'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_regex_findall_0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_regex_findall_0.py::test_regex_findall_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_regex_findall_0.py::test_regex_findall_mixed_parameters
============================== 2 failed in 0.55s ===============================
"""