
import pytest
from ansible.plugins.connection import paramiko_ssh
from unittest.mock import patch, MagicMock

# Assuming 'paramiko' is a required module for this connection to work correctly
try:
    import paramiko
except ImportError:
    paramiko = None

class TestConnectionParamikoSSH:
    
    @pytest.fixture(autouse=True)
    def setup_connection(self):
        if not paramiko:
            pytest.skip("paramiko is not installed")
        self.connection = paramiko_ssh.Connection()
        self.connection._play_context = {
            'remote_addr': '127.0.0.1',
            'remote_user': 'testuser',
            'private_key_file': '/path/to/private_key'
        }
    
    def test_connect_uncached_default_parameters(self):
        with patch('paramiko.SSHClient.connect') as mock_connect:
            ssh_client = self.connection._connect_uncached()
            assert isinstance(ssh_client, paramiko.SSHClient)
            mock_connect.assert_called_once_with(
                '127.0.0.1',
                username='testuser',
                allow_agent=True,
                look_for_keys=True,
                key_filename='/path/to/private_key',
                password=None,
                timeout=30,  # default timeout from paramiko
                port=22,     # default port for SSH
            )
    
    def test_connect_uncached_specified_port(self):
        self.connection._play_context['port'] = 2222
        with patch('paramiko.SSHClient.connect') as mock_connect:
            ssh_client = self.connection._connect_uncached()
            assert isinstance(ssh_client, paramiko.SSHClient)
            mock_connect.assert_called_once_with(
                '127.0.0.1',
                username='testuser',
                allow_agent=True,
                look_for_keys=True,
                key_filename='/path/to/private_key',
                password=None,
                timeout=30,  # default timeout from paramiko
                port=2222,   # specified port
            )
    
    def test_connect_uncached_with_password(self):
        self.connection._play_context['password'] = 'testpass'
        with patch('paramiko.SSHClient.connect') as mock_connect:
            ssh_client = self.connection._connect_uncached()
            assert isinstance(ssh_client, paramiko.SSHClient)
            mock_connect.assert_called_once_with(
                '127.0.0.1',
                username='testuser',
                allow_agent=False,  # agent should be disabled due to password presence
                look_for_keys=True,
                key_filename='/path/to/private_key',
                password='testpass',
                timeout=30,  # default timeout from paramiko
                port=22,     # default port for SSH
            )
