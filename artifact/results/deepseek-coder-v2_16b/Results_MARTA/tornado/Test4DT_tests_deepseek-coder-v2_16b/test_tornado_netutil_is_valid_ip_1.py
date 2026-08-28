
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

# Test cases for valid and invalid IP addresses

def test_valid_ipv4():
    ip = '192.168.1.1'
    assert is_valid_ip(ip) == True, f"Expected True for valid IPv4 address {ip}"

def test_valid_ipv6():
    ip = '2001:db8::1'
    assert is_valid_ip(ip) == True, f"Expected True for valid IPv6 address {ip}"

def test_invalid_empty_string():
    ip = ''
    assert is_valid_ip(ip) == False, f"Expected False for empty string IP address {ip}"

def test_invalid_domain_name():
    ip = 'localhost'
    assert is_valid_ip(ip) == False, f"Expected False for domain name IP address {ip}"

def test_invalid_string_with_null_bytes():
    ip = '192.168.1.1\x00'
    assert is_valid_ip(ip) == False, f"Expected False for IP address with null bytes {ip}"
