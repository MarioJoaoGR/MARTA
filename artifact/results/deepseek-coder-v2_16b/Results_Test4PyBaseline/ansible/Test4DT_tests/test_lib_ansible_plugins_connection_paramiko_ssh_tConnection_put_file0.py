# Module: ansible.plugins.connection.paramiko_ssh
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.errors import AnsibleFileNotFound, AnsibleError
import os
import paramiko

# Mocking necessary modules and classes for testing
@patch('ansible.plugins.connection.paramiko_ssh.to_bytes', lambda x, errors: x)
@patch('ansible.plugins.connection.paramiko_ssh.os.path.exists', return_value=True)
@patch('ansible.plugins.connection.paramiko_ssh.os.path.isfile', return_value=True)
class TestConnectionPutFile:
    
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.conn = Connection()
        self.conn._play_context = MagicMock()
        self.conn._play_context.remote_addr = '127.0.0.1'
    
    @patch('ansible.plugins.connection.paramiko_ssh.display')
    def test_put_file_success(self, mock_display):
        # Mocking the open_sftp method to return a SFTP client
        self.conn.ssh = MagicMock()
        sftp_client = MagicMock()
        self.conn.ssh.open_sftp.return_value = sftp_client
        
        in_path = 'local_file'
        out_path = '/remote/destination/file.txt'
        
        # Calling the method under test
        self.conn.put_file(in_path, out_path)
        
        # Assertions
        assert isinstance(self.conn.sftp, paramiko.SFTPClient)
        mock_display.vvv.assert_called_with("PUT %s TO %s" % (in_path, out_path), host='127.0.0.1')
    
    def test_put_file_file_not_found(self):
        # Mocking os.path.exists to return False
        with patch('ansible.plugins.connection.paramiko_ssh.os.path.exists', return_value=False):
            in_path = 'local_file'
            out_path = '/remote/destination/file.txt'
            
            # Calling the method under test and asserting the exception is raised
            with pytest.raises(AnsibleFileNotFound) as excinfo:
                self.conn.put_file(in_path, out_path)
                
            assert str(excinfo.value) == "file or module does not exist: %s" % in_path
    
    def test_put_file_open_sftp_failure(self):
        # Mocking the open_sftp method to raise an exception
        self.conn.ssh = MagicMock()
        self.conn.ssh.open_sftp.side_effect = Exception("Failed to open SFTP connection")
        
        in_path = 'local_file'
        out_path = '/remote/destination/file.txt'
        
        # Calling the method under test and asserting the exception is raised
        with pytest.raises(AnsibleError) as excinfo:
            self.conn.put_file(in_path, out_path)
            
        assert str(excinfo.value) == "failed to open a SFTP connection (%s)" % "Failed to open SFTP connection"
    
    def test_put_file_transfer_failure(self):
        # Mocking the sftp put method to raise an IOError
        self.conn.ssh = MagicMock()
        sftp_client = MagicMock()
        sftp_client.put.side_effect = IOError("Failed to transfer file")
        self.conn.ssh.open_sftp.return_value = sftp_client
        
        in_path = 'local_file'
        out_path = '/remote/destination/file.txt'
        
        # Calling the method under test and asserting the exception is raised
        with pytest.raises(AnsibleError) as excinfo:
            self.conn.put_file(in_path, out_path)
            
        assert str(excinfo.value) == "failed to transfer file to %s" % out_path

