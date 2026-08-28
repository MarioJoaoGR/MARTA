
import pytest
import socket
from unittest.mock import patch

def is_valid_ip(ip: str) -> bool:
    """Returns ``True`` if the given string is a well-formed IP address.

    Supports IPv4 and IPv6.
    """
    if not ip or "\x00" in ip:
        # getaddrinfo resolves empty strings to localhost, and truncates
        # on zero bytes.
        return False
    try:
        res = socket.getaddrinfo(
            ip, 0, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_NUMERICHOST
        )
        return bool(res)
    except socket.gaierror as e:
        if e.args[0] == socket.EAI_NONAME:
            return False
        raise
    return True

# Test cases for valid IPv4, valid IPv6, and invalid empty string scenarios

def test_valid_ipv4():
    assert is_valid_ip("192.168.1.1") == True

def test_valid_ipv6():
    assert is_valid_ip("2001:db8::1") == True

def test_invalid_empty_string():
    assert is_valid_ip("") == False
