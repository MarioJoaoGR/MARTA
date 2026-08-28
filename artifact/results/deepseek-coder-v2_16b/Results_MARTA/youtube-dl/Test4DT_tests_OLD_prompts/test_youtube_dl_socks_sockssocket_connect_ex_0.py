
import pytest
from unittest.mock import patch, MagicMock
import youtube_dl.socks

class sockssocket:
    def __init__(self):
        self._proxy = None

    def setproxy(self, proxy_type, host, port, username=None, password=None):
        if proxy_type == youtube_dl.socks.ProxyType.SOCKS4:
            self._proxy = MockSocks4Proxy(proxy_type, host, port, username, password)
        elif proxy_type == youtube_dl.socks.ProxyType.SOCKS5:
            self._proxy = MockSocks5Proxy(proxy_type, host, port, username, password)

    def connect_ex(self, address):
        if self._proxy is None:
            mock_socket = MagicMock()
            return mock_socket.connect_ex(address)
        else:
            proxy = self._proxy
            mock_socket = MagicMock()
            mock_socket.connect_ex.return_value = 0
            with patch('youtube_dl.socks.socket') as mock_socket_module:
                mock_socket_instance = mock_socket_module.socket.return_value
                mock_socket_instance.connect_ex.return_value = 0
                return proxy.connect_ex(address)

class MockSocks4Proxy:
    def __init__(self, proxy_type, host, port, username=None, password=None):
        self.type = proxy_type
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect_ex(self, address):
        return 0

class MockSocks5Proxy:
    def __init__(self, proxy_type, host, port, username=None, password=None):
        self.type = proxy_type
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect_ex(self, address):
        return 0


def test_connect_ex_with_socks4_proxy():
    sock = sockssocket()
    sock.setproxy(youtube_dl.socks.ProxyType.SOCKS4, '127.0.0.1', 9050)
    with patch('youtube_dl.socks.socket') as mock_socket:
        mock_socket.socket.return_value.connect_ex.return_value = 0
        result = sock.connect_ex(('www.example.com', 80))
        assert result == 0

def test_connect_ex_with_socks5_proxy():
    sock = sockssocket()
    sock.setproxy(youtube_dl.socks.ProxyType.SOCKS5, '127.0.0.1', 9050)
    with patch('youtube_dl.socks.socket') as mock_socket:
        mock_socket.socket.return_value.connect_ex.return_value = 0
        result = sock.connect_ex(('www.example.com', 80))
        assert result == 0

def test_connect_ex_with_socks5_proxy_auth():
    sock = sockssocket()
    sock.setproxy(youtube_dl.socks.ProxyType.SOCKS5, '127.0.0.1', 9050, username='user', password='pass')
    with patch('youtube_dl.socks.socket') as mock_socket:
        mock_socket.socket.return_value.connect_ex.return_value = 0
        result = sock.connect_ex(('www.example.com', 80))
        assert result == 0