
import pytest
from lib.ansible.executor.stats import AggregateStats


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        stats = AggregateStats()
        # Testing with None as the value
        stats.set_custom_stats('cpu_usage', None, 'host1')
        assert stats.custom == {'host1': {'cpu_usage': None}}
    
        # Testing with empty string as the value
        stats.set_custom_stats('', 0, 'host1')
>       assert stats.custom == {'host1': {''}}
E       AssertionError: assert {'host1': {''...usage': None}} == {'host1': {''}}
E         
E         Differing items:
E         {'host1': {'': 0, 'cpu_usage': None}} != {'host1': {''}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_0.py:13: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        stats = AggregateStats()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_0.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_0.py::test_invalid_input
============================== 2 failed in 0.23s ===============================
"""