
import pytest
from ansible.module_utils.urls import _ipaddress_match

# Test valid IPv4 address input
def test_valid_ipv4_address():
    ipname = '192.168.1.1\n'
    host_ip = b'\xc0\xa8\x01\x01'
    assert _ipaddress_match(ipname, host_ip) == True

# Test valid IPv6 address input
def test_valid_ipv6_address():
    ipname = '::1\n'
    host_ip = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
    assert _ipaddress_match(ipname, host_ip) == True

# Test invalid IP address input
def test_invalid_ip_address():
    ipname = 'invalid ip address'
    host_ip = b'\xc0\xa8\x01\x01'
    assert _ipaddress_match(ipname, host_ip) == False
