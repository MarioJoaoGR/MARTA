
import pytest
from ansible.plugins.connection.psrp import Connection

def test_valid_case():
    conn = Connection(remote_addr='192.168.1.100', remote_user='admin', remote_password='password')
    assert conn is not None
    assert conn.host == '192.168.1.100'
    assert conn.runspace is None
    assert conn._shell_type == 'powershell'
    assert conn.always_pipeline_modules is True
    assert conn.has_native_async is True

def test_edge_case():
    conn = Connection(remote_addr=None, remote_user='', remote_password='')
    assert conn is not None
    assert conn.host is None
    assert conn.runspace is None
    assert conn._shell_type == 'powershell'
    assert conn.always_pipeline_modules is True
    assert conn.has_native_async is True

def test_error_case():
    with pytest.raises(TypeError):
        conn = Connection(remote_addr='192.168.1.100', remote_user=None, remote_password='password')
