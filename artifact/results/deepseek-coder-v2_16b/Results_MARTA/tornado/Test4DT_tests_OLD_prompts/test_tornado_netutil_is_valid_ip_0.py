
import pytest
from unittest.mock import patch
import socket
from tornado.netutil import is_valid_ip

def test_valid_ipv4():
    with patch('socket.getaddrinfo', return_value=[{'family': socket.AF_INET, 'proto': socket.IPPROTO_TCP, 'socktype': socket.SOCK_STREAM, 'name': 'test', 'flags': socket.AI_NUMERICHOST}]):
        assert is_valid_ip("192.168.1.1") == True

def test_valid_ipv6():
    with patch('socket.getaddrinfo', return_value=[{'family': socket.AF_INET6, 'proto': socket.IPPROTO_TCP, 'socktype': socket.SOCK_STREAM, 'name': 'test', 'flags': socket.AI_NUMERICHOST}]):
        assert is_valid_ip("2001:db8::1") == True

def test_invalid_empty_string():
    with patch('socket.getaddrinfo', side_effect=socket.gaierror(socket.EAI_NONAME, 'Name or service not known')):
        assert is_valid_ip("") == False
