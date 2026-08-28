
import pytest
from mimesis.providers import Internet
from ipaddress import IPv4Address

@pytest.fixture(scope="module")
def internet():
    return Internet()

def test_ip_v4_object_generates_valid_ipv4_address(internet):
    ipv4 = internet.ip_v4_object()
    assert isinstance(ipv4, IPv4Address)

def test_ip_v4_object_within_range(internet):
    ipv4 = internet.ip_v4_object()
    max_ipv4 = (2 ** 32) - 1
    assert 0 <= int(ipv4) <= max_ipv4

def test_ip_v4_object_unique_values(internet):
    ipv4s = [internet.ip_v4_object() for _ in range(5)]
    unique_ipv4s = set(map(str, ipv4s))
    assert len(unique_ipv4s) == len(ipv4s)
