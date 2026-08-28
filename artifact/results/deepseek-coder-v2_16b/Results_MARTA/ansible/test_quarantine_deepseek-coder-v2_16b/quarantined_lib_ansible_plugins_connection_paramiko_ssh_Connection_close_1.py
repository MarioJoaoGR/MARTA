
import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
import os
import paramiko

@pytest.fixture(scope="module")
def connection():
    conn = Connection()
    yield conn
    # Ensure the connection is closed after all tests in this module are done
    conn.close()

def test_connection_transport(connection):
    assert connection.transport == 'paramiko'

def test_cache_key_generation(connection):
    cache_key = connection._cache_key()
    expected_cache_key = f"{connection.host}:{connection.user}"
    assert cache_key == expected_cache_key

def test_close_method(connection):
    # Ensure the connection is open before closing
    assert connection._connected
    
    connection.close()
    
    # Check if the connection is closed after calling close method
    assert not connection._connected

def test_save_ssh_host_keys(monkeypatch, connection):
    # Mock paramiko SSH client to simulate adding host keys
    class MockSSHClient:
        def __init__(self):
            self.load_system_host_keys = lambda: None
            self._system_host_keys = {}
            self._host_keys = {'some_key': 'some_value'}  # Simulate added keys
        
        def close(self):
            pass
    
    monkeypatch.setattr(paramiko, "SSHClient", MockSSHClient)
    
    # Ensure the keyfile exists and is writable for testing purposes
    connection.keyfile = "/tmp/known_hosts"
    os.makedirs("/tmp", exist_ok=True)
    open(connection.keyfile, 'a').close()
    
    connection._save_ssh_host_keys(connection.keyfile)
    
    # Check if the keys were added correctly
    with open(connection.keyfile, 'r') as f:
        content = f.read()
    assert "some_key" in content

def test_reset_method(monkeypatch, connection):
    # Mock paramiko SSH client to simulate closing and reopening the connection
    class MockSSHClient:
        def __init__(self):
            self.load_system_host_keys = lambda: None
            self._system_host_keys = {}
        
        def close(self):
            pass
        
        def _connect(self):
            connection._connected = True
    
    monkeypatch.setattr(paramiko, "SSHClient", MockSSHClient)
    
    # Ensure the connection is closed before resetting
    assert not connection._connected
    
    connection.reset()
    
    # Check if the connection is re-opened after calling reset method
    assert connection._connected

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
_ ERROR collecting test_lib_ansible_plugins_connection_paramiko_ssh_Connection_close_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_connection_paramiko_ssh_Connection_close_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_connection_paramiko_ssh_Connection_close_1.py:5: in <module>
    import paramiko
E   ModuleNotFoundError: No module named 'paramiko'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_connection_paramiko_ssh_Connection_close_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.97s ===============================
"""