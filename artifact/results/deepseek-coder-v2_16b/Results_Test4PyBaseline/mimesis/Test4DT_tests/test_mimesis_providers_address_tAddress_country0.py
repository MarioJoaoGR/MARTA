
import pytest
from mimesis.providers.address import Address

# Test cases for the country method in the Address class
def test_country_default():
    address = Address()
    assert isinstance(address.country(), str)
    # Assuming default locale is en_US and its country is United States