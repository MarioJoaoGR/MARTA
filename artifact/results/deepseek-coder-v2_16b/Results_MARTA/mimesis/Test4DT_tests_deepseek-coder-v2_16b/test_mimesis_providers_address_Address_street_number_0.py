
import pytest
from mimesis.providers.address import Address

# Test for valid input with default maximum value
def test_valid_input():
    address_instance = Address()
    street_number = address_instance.street_number()
    assert isinstance(street_number, str), "Expected a string representation of the number"
    assert 1 <= int(street_number) <= 1400, f"Expected a number between 1 and 1400, but got {street_number}"

# Test for edge case with maximum set to 1
def test_edge_case():
    address_instance = Address()
    street_number = address_instance.street_number(maximum=1)
    assert isinstance(street_number, str), "Expected a string representation of the number"
    assert 1 <= int(street_number) <= 1, f"Expected a number between 1 and 1, but got {street_number}"

# Test for invalid input with negative maximum value
def test_invalid_input():
    address_instance = Address()
    with pytest.raises(ValueError):
        address_instance.street_number(maximum=-500)
