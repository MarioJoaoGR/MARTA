
import pytest
from ansible.executor.stats import AggregateStats


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_set_custom_stats _____________________________

    def test_set_custom_stats():
        stats = AggregateStats()
        # Test setting custom statistics for a specific host
        stats.set_custom_stats('memory_usage', 128, 'host1')
>       assert stats.custom == {'_run': {}, 'host1': {'memory_usage': 128}}
E       AssertionError: assert {'host1': {'m..._usage': 128}} == {'_run': {}, ..._usage': 128}}
E         
E         Omitting 1 identical items, use -vv to show
E         Right contains 1 more item:
E         {'_run': {}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_1.py:9: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        stats = AggregateStats()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_1.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_1.py::test_set_custom_stats
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_stats_AggregateStats_set_custom_stats_1.py::test_invalid_input
============================== 2 failed in 0.65s ===============================
"""