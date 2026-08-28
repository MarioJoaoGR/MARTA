# Module: ansible.plugins.connection.psrp
import pytest
from ansible.plugins.connection.psrp import Connection

# Test initialization with default parameters
def test_default_init():
    conn = Connection()
    assert conn.always_pipeline_modules is True
    assert conn.has_native_async is True
    assert conn.runspace is None
    assert conn.host is None
    assert conn._last_pipeline is False
    assert conn._shell_type == 'powershell'

# Test initialization with host parameter
def test_init_with_host():
    conn = Connection(host='remote_host')
    assert conn.always_pipeline_modules is True
    assert conn.has_native_async is True
    assert conn.runspace is None
    assert conn.host == 'remote_host'
    assert conn._last_pipeline is False
    assert conn._shell_type == 'powershell'

# Test initialization with additional parameters (not recommended, but should not raise errors)
def test_init_with_additional_params():
    try:
        conn = Connection(host='remote_host', remote_user='username', remote_password='password')
        assert conn.always_pipeline_modules is True
        assert conn.has_native_async is True
        assert conn.runspace is None
        assert conn.host == 'remote_host'
        assert conn._last_pipeline is False
        assert conn._shell_type == 'powershell'
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")

# Test initialization with invalid parameters (should raise TypeError)
def test_init_with_invalid_params():
    with pytest.raises(TypeError):
        conn = Connection(invalid_param='invalid')
