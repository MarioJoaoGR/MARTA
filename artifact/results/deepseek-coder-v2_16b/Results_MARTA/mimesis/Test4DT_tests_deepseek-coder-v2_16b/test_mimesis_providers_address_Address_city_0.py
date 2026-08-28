
import pytest
from mimesis.providers import Address

# Test retrieving a random city from the address data
def test_valid_city():
    addr = Address()
    city = addr.city()
    assert isinstance(city, str), "Expected a string representation of a city"
    assert len(city) > 0, "City name should not be empty"

# Test handling an empty list for cities
def test_empty_city_list():
    # Create a modified instance with an empty 'city' list
    addr = Address()
    addr._data['city'] = []
    with pytest.raises(IndexError):
        city = addr.city()

# Test behavior with an invalid instance type
def test_invalid_instance():
    # Create a string instead of an Address instance
    invalid_addr = "Invalid address"
    with pytest.raises(AttributeError):
        city = invalid_addr.city()
