
import pytest
from lib.ansible.executor.task_result import TaskResult


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult__check_key_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_key_exists _____________________________

    def test_valid_key_exists():
        task_result = TaskResult('example_host', {'task': 'example_task'}, {'results': [{'key1': 'value1'}, {'key2': 'value2'}]})
>       assert task_result._check_key('key1') == 'value1'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult__check_key_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <lib.ansible.executor.task_result.TaskResult object at 0x7f0a8be0f1c0>
key = 'key1'

    def _check_key(self, key):
        '''get a specific key from the result or its items'''
    
        if isinstance(self._result, dict) and key in self._result:
            return self._result.get(key, False)
        else:
            flag = False
            for res in self._result.get('results', []):
                if isinstance(res, dict):
>                   flag |= res.get(key, False)
E                   TypeError: unsupported operand type(s) for |=: 'bool' and 'str'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/task_result.py:105: TypeError
________________________ test_valid_key_in_nested_list _________________________

    def test_valid_key_in_nested_list():
        task_result = TaskResult('example_host', {'task': 'example_task'}, {'results': [{'key1': 'value1'}, {'key2': 'value2'}]})
>       assert task_result._check_key('key2') == 'value2'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult__check_key_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <lib.ansible.executor.task_result.TaskResult object at 0x7f0a8d3e8f10>
key = 'key2'

    def _check_key(self, key):
        '''get a specific key from the result or its items'''
    
        if isinstance(self._result, dict) and key in self._result:
            return self._result.get(key, False)
        else:
            flag = False
            for res in self._result.get('results', []):
                if isinstance(res, dict):
>                   flag |= res.get(key, False)
E                   TypeError: unsupported operand type(s) for |=: 'bool' and 'str'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/task_result.py:105: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult__check_key_0.py::test_valid_key_exists
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_task_result_TaskResult__check_key_0.py::test_valid_key_in_nested_list
============================== 2 failed in 0.29s ===============================
"""