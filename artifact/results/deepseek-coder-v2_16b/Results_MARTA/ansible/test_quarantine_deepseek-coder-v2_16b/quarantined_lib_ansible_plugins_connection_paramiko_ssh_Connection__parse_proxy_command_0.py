
import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
import paramiko

@pytest.fixture
def connection():
    return Connection()

def test_parse_proxy_command_default_port(connection):
    sock_kwarg = connection._parse_proxy_command()
    assert isinstance(sock_kwarg, dict)
    if sock_kwarg:
        assert 'sock' in sock_kwarg
        assert isinstance(sock_kwarg['sock'], paramiko.ProxyCommand)

def test_parse_proxy_command_custom_port(connection):
    sock_kwarg = connection._parse_proxy_command(port=2299)
    assert isinstance(sock_kwarg, dict)
    if sock_kwarg:
        assert 'sock' in sock_kwarg
        assert isinstance(sock_kwarg['sock'], paramiko.ProxyCommand)

def test_parse_proxy_command_no_proxy_command(connection):
    connection._play_context.ssh_common_args = ''
    sock_kwarg = connection._parse_proxy_command()
    assert isinstance(sock_kwarg, dict)
    assert 'sock' not in sock_kwarg

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
_ ERROR collecting test_lib_ansible_plugins_connection_paramiko_ssh_Connection__parse_proxy_command_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_connection_paramiko_ssh_Connection__parse_proxy_command_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_connection_paramiko_ssh_Connection__parse_proxy_command_0.py:4: in <module>
    import paramiko
E   ModuleNotFoundError: No module named 'paramiko'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_connection_paramiko_ssh_Connection__parse_proxy_command_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.59s ===============================
"""