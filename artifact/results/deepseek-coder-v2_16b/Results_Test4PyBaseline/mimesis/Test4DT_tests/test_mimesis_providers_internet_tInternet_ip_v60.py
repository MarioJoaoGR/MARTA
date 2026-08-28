# Module: mimesis.providers.internet
# test_internet.py
from mimesis.providers.internet import Internet
import pytest

@pytest.fixture
def internet():
    return Internet()

def test_default_ipv6(internet):
    ipv6_address = internet.ip_v6()
    assert isinstance(ipv6_address, str), "Expected an IPv6 address string"

def test_custom_seed_ipv6(internet):
    custom_internet = Internet(seed=12345)
    ipv6_address = custom_internet.ip_v6()
    assert isinstance(ipv6_address, str), "Expected an IPv6 address string"

def test_multiple_calls_ipv6(internet):
    ipv6_addresses = [internet.ip_v6() for _ in range(5)]
    unique_addresses = set(ipv6_addresses)
    assert len(unique_addresses) > 1, "Expected multiple unique IPv6 addresses"
