
import pytest
from ansible.plugins.callback import default

@pytest.fixture(scope="module")
def callback_instance():
    return default.CallbackModule()



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_cleanup_task_start_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

callback_instance = <ansible.plugins.callback.default.CallbackModule object at 0x7f2b8f8bc8e0>

    def test_valid_inputs(callback_instance):
        task = {"name": "example_task", "type": "run"}
>       callback_instance._task_start(task, prefix='TASK')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_cleanup_task_start_1.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.callback.default.CallbackModule object at 0x7f2b8f8bc8e0>
task = {'name': 'example_task', 'type': 'run'}, prefix = 'TASK'

    def _task_start(self, task, prefix=None):
        # Cache output prefix for task if provided
        # This is needed to properly display 'RUNNING HANDLER' and similar
        # when hiding skipped/ok task results
        if prefix is not None:
>           self._task_type_cache[task._uuid] = prefix
E           AttributeError: 'dict' object has no attribute '_uuid'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/callback/default.py:175: AttributeError
________________________________ test_edge_case ________________________________

callback_instance = <ansible.plugins.callback.default.CallbackModule object at 0x7f2b8f8bc8e0>

    def test_edge_case(callback_instance):
        with pytest.raises(TypeError):
>           callback_instance._task_start(None, prefix='TASK')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_cleanup_task_start_1.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.callback.default.CallbackModule object at 0x7f2b8f8bc8e0>
task = None, prefix = 'TASK'

    def _task_start(self, task, prefix=None):
        # Cache output prefix for task if provided
        # This is needed to properly display 'RUNNING HANDLER' and similar
        # when hiding skipped/ok task results
        if prefix is not None:
>           self._task_type_cache[task._uuid] = prefix
E           AttributeError: 'NoneType' object has no attribute '_uuid'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/callback/default.py:175: AttributeError
_____________________________ test_invalid_inputs ______________________________

callback_instance = <ansible.plugins.callback.default.CallbackModule object at 0x7f2b8f8bc8e0>

    def test_invalid_inputs(callback_instance):
        with pytest.raises(TypeError):
>           callback_instance._task_start("not a task", prefix='TASK')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_cleanup_task_start_1.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.callback.default.CallbackModule object at 0x7f2b8f8bc8e0>
task = 'not a task', prefix = 'TASK'

    def _task_start(self, task, prefix=None):
        # Cache output prefix for task if provided
        # This is needed to properly display 'RUNNING HANDLER' and similar
        # when hiding skipped/ok task results
        if prefix is not None:
>           self._task_type_cache[task._uuid] = prefix
E           AttributeError: 'str' object has no attribute '_uuid'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/callback/default.py:175: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_cleanup_task_start_1.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_cleanup_task_start_1.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_cleanup_task_start_1.py::test_invalid_inputs
============================== 3 failed in 0.97s ===============================
"""