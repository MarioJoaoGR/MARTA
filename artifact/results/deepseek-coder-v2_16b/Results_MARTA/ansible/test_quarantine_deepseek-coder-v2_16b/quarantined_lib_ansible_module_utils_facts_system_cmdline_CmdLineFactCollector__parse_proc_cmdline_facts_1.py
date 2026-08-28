
import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        collector = CmdLineFactCollector()
        result = collector._parse_proc_cmdline_facts('arg1=value1 arg2 arg3=value3')
>       assert result == {'arg1': 'value1', 'arg2': True, 'arg3': ['value3']}
E       AssertionError: assert {'arg1': 'val...g3': 'value3'} == {'arg1': 'val...': ['value3']}
E         
E         Omitting 2 identical items, use -vv to show
E         Differing items:
E         {'arg3': 'value3'} != {'arg3': ['value3']}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_1.py:8: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        collector = CmdLineFactCollector()
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_1.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_cmdline_CmdLineFactCollector__parse_proc_cmdline_facts_1.py::test_invalid_input
============================== 2 failed in 0.71s ===============================
"""