
import pytest
from mimesis.providers.address import Address

# Test initialization without locale specification
def test_default_initialization():
    address = Address()
    assert hasattr(address, 'city'), "Address instance should have a city method"
    city = address.city()