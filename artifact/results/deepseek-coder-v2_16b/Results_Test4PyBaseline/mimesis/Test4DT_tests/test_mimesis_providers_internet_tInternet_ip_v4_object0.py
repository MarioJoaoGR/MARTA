
import pytest
from mimesis import Internet
from ipaddress import IPv4Address

# Fixture to create an instance of the Internet class with a default seed
@pytest.fixture
def internet():
    return Internet()

# Test case for generating a random IPv4 address object with default settings
def test_ip_v4_object_default(internet):
    ipv4_address_obj = internet.ip_v4_object()
    assert isinstance(ipv4_address_obj, IPv4Address), "Expected an instance of IPv4Address"

# Test case for generating a random IPv4 address object with a custom seed
def test_ip_v4_object_custom_seed(internet):
    internet_with_seed = Internet(seed=12345)
    ipv4_address_obj_custom_seed = internet_with_seed.ip_v4_object()
    assert isinstance(ipv4_address_obj_custom_seed, IPv4Address), "Expected an instance of IPv4Address"
    assert int(ipv4_address_obj_custom_seed) != int(internet.ip_v4_object()), "Custom seed should generate a different IP address"

# Test case for ensuring the method generates a valid IPv4 address within the allowed range
def test_ip_v4_object_within_range(internet):
    ipv4_address_obj = internet.ip_v4_object()
    assert 0 <= int(ipv4_address_obj) <= (2 ** 32) - 1, "Generated IP address is not within the valid range"
