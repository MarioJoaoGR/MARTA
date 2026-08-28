# Module: ansible.plugins.connection.psrp
import pytest
from ansible.plugins.connection import Connection

# Fixture to create a new connection instance for testing
@pytest.fixture
def conn():
    return Connection(host='remote_host', remote_user='username', remote_password='password')

# Test case to check if the connection is initialized correctly
def test_connection_initialization(conn):
    assert conn.host == 'remote_host'
    assert conn.remote_user == 'username'
    assert conn.remote_password == 'password'
    assert conn.always_pipeline_modules is True
    assert conn.has_native_async is True

# Test case to check if the _put_file_old method raises an error when the file does not exist locally
def test_put_file_local_file_not_found(conn):
    with pytest.raises(AnsibleFileNotFound) as excinfo:
        conn._put_file_old('non_existent_path', 'remote_path')
    assert "file or module does not exist" in str(excinfo.value)

# Test case to check if the _put_file_old method returns correct return code, stdout, stderr, and SHA1 hash when a valid file is uploaded
def test_put_file_valid_file(conn):
    # Assuming 'local_path' exists and contains some data
    local_path = 'local_path'
    remote_path = 'remote_path'
    expected_rc, _, _, expected_sha1 = conn._put_file_old(local_path, remote_path)
    
    # Additional assertions can be added here to validate the file transfer and checksum
    assert isinstance(expected_rc, int)
    assert len(expected_sha1) == 40  # SHA1 hash length is 40 characters
