
import pytest
from mimesis.providers import internet

# Test for valid IPv4 without port
def test_valid_ipv4_without_port():
    internet_provider = internet.Internet()
    ipv4 = internet_provider.ip_v4()
    assert isinstance(ipv4, str), "Expected a string representation of an IP address"
    assert len(ipv4.split('.')) == 4, "Expected exactly four octets in the IPv4 address"

# Test for valid IPv4 with port
def test_valid_ipv4_with_port():
    internet_provider = internet.Internet()
    ipv4_with_port = internet_provider.ip_v4(with_port=True)
    parts = ipv4_with_port.split(':')
    assert isinstance(parts[1], str), "Expected the port to be a string"
    assert len(parts) == 2, "Expected exactly two parts in the IPv4 address with port"

# Test for invalid input (None)
def test_invalid_input_none():
    internet_provider = internet.Internet()
    with pytest.raises(TypeError):
        ipv4_with_port = internet_provider.ip_v4(with_port=True, port_range=None)
