
import pytest
from lib.ansible.plugins.callback import HostData
import time

def test_hostdata_initialization():
    uuid = '1234-5678-90AB'
    name = 'HostA'
    status = 'running'
    result = {'cpu_usage': 75, 'memory_usage': 80}
    
    host = HostData(uuid, name, status, result)
    
    assert host.uuid == uuid
    assert host.name == name
    assert host.status == status
    assert host.result == result
    assert isinstance(host.finish, float)

def test_hostdata_default_finish():
    uuid = '1234-5678-90AB'
    name = 'HostA'
    status = 'running'
    result = {'cpu_usage': 75, 'memory_usage': 80}
    
    host = HostData(uuid, name, status, result)
    
    assert isinstance(host.finish, float)
    # Check that finish is set to the current time when the instance is created
    assert host.finish != 0

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
_ ERROR collecting test_lib_ansible_plugins_callback_junit_HostData___init___0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_HostData___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_HostData___init___0.py:3: in <module>
    from lib.ansible.plugins.callback import HostData
E   ImportError: cannot import name 'HostData' from 'lib.ansible.plugins.callback' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/callback/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_callback_junit_HostData___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.48s ===============================
"""