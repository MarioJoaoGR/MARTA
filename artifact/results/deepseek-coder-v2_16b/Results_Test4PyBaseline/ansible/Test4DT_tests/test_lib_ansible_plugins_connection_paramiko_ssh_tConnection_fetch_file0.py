# Module: ansible.plugins.connection.paramiko_ssh
import pytest
from ansible.plugins.connection import Connection
from unittest.mock import patch, MagicMock

# Test the fetch_file method of the Connection class
def test_fetch_file():
    # Create a mock instance of the Connection class
    conn = Connection()
    
    # Mock the necessary methods and attributes for testing
    conn._play_context = MagicMock()
    conn._connect_sftp = MagicMock(return_value=MagicMock())
    conn.sftp = MagicMock()
    conn.sftp.get = MagicMock()
    
    # Define the in_path and out_path for the test
    in_path = '/remote/path/to/file'
    out_path = '/local/path/to/save/file'
    
    # Call the fetch_file method
    conn.fetch_file(in_path, out_path)
    
    # Assert that _connect_sftp was called once with no arguments
    conn._connect_sftp.assert_called_once()
    
    # Assert that sftp.get was called with the correct arguments
    conn.sftp.get.assert_called_once_with(to_bytes(in_path, errors='surrogate_or_strict'), to_bytes(out_path, errors='surrogate_or_strict'))
    
    # Add a patch for display.vvv to ensure it is called with the correct arguments
    with patch('ansible.plugins.connection.display.vvv') as mock_display:
        conn.fetch_file(in_path, out_path)
        mock_display.assert_called_once_with("FETCH %s TO %s" % (in_path, out_path), host=conn._play_context.remote_addr)

# Test the fetch_file method with an exception in _connect_sftp
def test_fetch_file_exception():
    # Create a mock instance of the Connection class
    conn = Connection()
    
    # Mock the necessary methods and attributes for testing
    conn._play_context = MagicMock()
    conn._connect_sftp = MagicMock(side_effect=Exception("Failed to connect"))
    
    # Define the in_path and out_path for the test
    in_path = '/remote/path/to/file'
    out_path = '/local/path/to/save/file'
    
    # Assert that calling fetch_file raises AnsibleError with the correct message
    with pytest.raises(AnsibleError, match="failed to open a SFTP connection \(Failed to connect\)") as excinfo:
        conn.fetch_file(in_path, out_path)
    
    # Assert that _connect_sftp was called once with no arguments
    conn._connect_sftp.assert_called_once()

# Test the fetch_file method with an exception in sftp.get
def test_fetch_file_ioerror():
    # Create a mock instance of the Connection class
    conn = Connection()
    
    # Mock the necessary methods and attributes for testing
    conn._play_context = MagicMock()
    conn._connect_sftp = MagicMock(return_value=MagicMock())
    conn.sftp.get = MagicMock(side_effect=IOError("Failed to transfer"))
    
    # Define the in_path and out_path for the test
    in_path = '/remote/path/to/file'
    out_path = '/local/path/to/save/file'
    
    # Assert that calling fetch_file raises AnsibleError with the correct message
    with pytest.raises(AnsibleError, match="failed to transfer file from /remote/path/to/file") as excinfo:
        conn.fetch_file(in_path, out_path)
    
    # Assert that sftp.get was called once with the correct arguments
    conn.sftp.get.assert_called_once_with(to_bytes(in_path, errors='surrogate_or_strict'), to_bytes(out_path, errors='surrogate_or_strict'))
