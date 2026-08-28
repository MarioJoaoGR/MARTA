
import pytest
from ansible.plugins.callback import CallbackModule

class TestCallbackModule:
    @pytest.fixture(autouse=True)
    def setup_module(self):
        self.callback = CallbackModule()
    
    def test_v2_playbook_on_handler_task_start(self):
        # Create a mock task dictionary
        task = {
            'name': 'sample_task',
            'type': 'run'
        }
        
        # Call the method under test
        self.callback.v2_playbook_on_handler_task_start(task)
        
        # Assert that _task_start was called with the correct prefix
        assert self.callback._last_task_name == 'RUNNING HANDLER sample_task'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_handler_task_start_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_handler_task_start_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_handler_task_start_0.py:3: in <module>
    from ansible.plugins.callback import CallbackModule
E   ImportError: cannot import name 'CallbackModule' from 'ansible.plugins.callback' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/callback/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_default_CallbackModule_v2_playbook_on_handler_task_start_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.57s ===============================
"""