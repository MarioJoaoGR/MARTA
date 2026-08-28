
import pytest
import datetime
import time
from ansible.module_utils.facts.system.date_time import DateTimeFactCollector



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_date_time_DateTimeFactCollector_collect_2.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        collector = DateTimeFactCollector()
        collected_facts = {}
        result = collector.collect(collected_facts=collected_facts)
    
        assert 'date_time' in result
        date_time_facts = result['date_time']
        now = datetime.datetime.now()
    
        assert 'year' in date_time_facts
        assert date_time_facts['year'] == now.strftime('%Y')
        assert 'month' in date_time_facts
        assert date_time_facts['month'] == now.strftime('%m')
        assert 'weekday' in date_time_facts
        assert date_time_facts['weekday'] == now.strftime('%A')
        assert 'weekday_number' in date_time_facts
        assert date_time_facts['weekday_number'] == now.strftime('%w')
        assert 'weeknumber' in date_time_facts
        assert date_time_facts['weeknumber'] == now.strftime('%W')
        assert 'day' in date_time_facts
        assert date_time_facts['day'] == now.strftime('%d')
        assert 'hour' in date_time_facts
        assert date_time_facts['hour'] == now.strftime('%H')
        assert 'minute' in date_time_facts
        assert date_time_facts['minute'] == now.strftime('%M')
        assert 'second' in date_time_facts
        assert date_time_facts['second'] == now.strftime('%S')
        assert 'epoch' in date_time_facts
        epoch_str = str(int(time.time()))
        if date_time_facts['epoch'] == '' or date_time_facts['epoch'][0] == '%':
            date_time_facts['epoch'] = epoch_str
        assert 'iso8601_micro' in date_time_facts
        iso8601_micro = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
>       assert date_time_facts['iso8601_micro'] == iso8601_micro
E       AssertionError: assert '2026-07-28T09:25:04.872289Z' == '2026-07-28T10:25:04.872358Z'
E         
E         - 2026-07-28T10:25:04.872358Z
E         ?            -           ^^
E         + 2026-07-28T09:25:04.872289Z
E         ?             +          ^ +

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_date_time_DateTimeFactCollector_collect_2.py:40: AssertionError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        collector = DateTimeFactCollector()
        collected_facts = None
    
        result_none = collector.collect(collected_facts=collected_facts)
        assert 'date_time' in result_none
        date_time_facts_none = result_none['date_time']
        now = datetime.datetime.now()
    
        assert 'year' in date_time_facts_none
        assert date_time_facts_none['year'] == now.strftime('%Y')
        assert 'month' in date_time_facts_none
        assert date_time_facts_none['month'] == now.strftime('%m')
        assert 'weekday' in date_time_facts_none
        assert date_time_facts_none['weekday'] == now.strftime('%A')
        assert 'weekday_number' in date_time_facts_none
        assert date_time_facts_none['weekday_number'] == now.strftime('%w')
        assert 'weeknumber' in date_time_facts_none
        assert date_time_facts_none['weeknumber'] == now.strftime('%W')
        assert 'day' in date_time_facts_none
        assert date_time_facts_none['day'] == now.strftime('%d')
        assert 'hour' in date_time_facts_none
        assert date_time_facts_none['hour'] == now.strftime('%H')
        assert 'minute' in date_time_facts_none
        assert date_time_facts_none['minute'] == now.strftime('%M')
        assert 'second' in date_time_facts_none
        assert date_time_facts_none['second'] == now.strftime('%S')
        assert 'epoch' in date_time_facts_none
        epoch_str = str(int(time.time()))
        if date_time_facts_none['epoch'] == '' or date_time_facts_none['epoch'][0] == '%':
            date_time_facts_none['epoch'] = epoch_str
        assert 'iso8601_micro' in date_time_facts_none
        iso8601_micro = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
>       assert date_time_facts_none['iso8601_micro'] == iso8601_micro
E       AssertionError: assert '2026-07-28T09:25:04.902505Z' == '2026-07-28T10:25:04.902561Z'
E         
E         - 2026-07-28T10:25:04.902561Z
E         ?            -            ^^
E         + 2026-07-28T09:25:04.902505Z
E         ?             +           ^^

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_date_time_DateTimeFactCollector_collect_2.py:75: AssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        collector = DateTimeFactCollector()
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_date_time_DateTimeFactCollector_collect_2.py:80: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_date_time_DateTimeFactCollector_collect_2.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_date_time_DateTimeFactCollector_collect_2.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_date_time_DateTimeFactCollector_collect_2.py::test_invalid_inputs
============================== 3 failed in 0.73s ===============================
"""