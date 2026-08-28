
import pytest
from ansible.module_utils.facts.collector import get_collector_names


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_get_collector_names_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_get_collector_names_default _______________________

    def test_get_collector_names_default():
        result = get_collector_names()
>       assert result == frozenset(['all'])
E       AssertionError: assert set() == frozenset({'all'})
E         
E         Extra items in the right set:
E         'all'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_get_collector_names_0.py:7: AssertionError
____________________ test_get_collector_names_excluding_all ____________________

    def test_get_collector_names_excluding_all():
        result = get_collector_names(gather_subset=['!all'])
>       assert result == frozenset(['min'])
E       AssertionError: assert set() == frozenset({'min'})
E         
E         Extra items in the right set:
E         'min'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_get_collector_names_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_get_collector_names_0.py::test_get_collector_names_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_get_collector_names_0.py::test_get_collector_names_excluding_all
============================== 2 failed in 0.32s ===============================
"""