
import pytest
from ansible.plugins.callback import CallbackModule
from unittest.mock import patch

@pytest.fixture(scope="module")
def callback_module():
    return CallbackModule()

def test_v2_runner_on_ok_with_changes(callback_module):
    result = {
        '_result': {'changed': True, 'ansible_job_id': "12345", 'results': {...}},
        '_host': Host('localhost'),
        '_task': Task(action='some_module')
    }
    with patch('sys.stdout', new=StringIO()) as fake_output:
        callback_module.v2_runner_on_ok(result)
        assert "localhost | CHANGED =>" in fake_output.getvalue()

def test_v2_runner_on_ok_without_changes(callback_module):
    result = {
        '_result': {'changed': False, 'ansible_job_id': "12345", 'results': {...}},
        '_host': Host('localhost'),
        '_task': Task(action='some_module')
    }
    with patch('sys.stdout', new=StringIO()) as fake_output:
        callback_module.v2_runner_on_ok(result)
        assert "localhost | SUCCESS =>" in fake_output.getvalue()

def test_v2_runner_on_ok_no_ansible_job_id(callback_module):
    result = {
        '_result': {'changed': True, 'results': {...}},
        '_host': Host('localhost'),
        '_task': Task(action='some_module')
    }
    with patch('sys.stdout', new=StringIO()) as fake_output:
        callback_module.v2_runner_on_ok(result)
        assert "localhost | CHANGED =>" in fake_output.getvalue()

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
_ ERROR collecting test_lib_ansible_plugins_callback_minimal_CallbackModule_v2_runner_on_ok_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_minimal_CallbackModule_v2_runner_on_ok_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_minimal_CallbackModule_v2_runner_on_ok_1.py:3: in <module>
    from ansible.plugins.callback import CallbackModule
E   ImportError: cannot import name 'CallbackModule' from 'ansible.plugins.callback' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/callback/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_minimal_CallbackModule_v2_runner_on_ok_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.97s ===============================
"""