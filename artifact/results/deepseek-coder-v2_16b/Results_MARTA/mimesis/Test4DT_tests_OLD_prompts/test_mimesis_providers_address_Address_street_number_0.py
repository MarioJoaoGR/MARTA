
import pytest
from unittest.mock import patch
from mimesis.providers.address import Address

# Test for valid input with default maximum value
def test_valid_input():
    address = Address()
    street_number = address.street_number()
    assert isinstance(street_number, str)
    number = int(street_number)
    assert 1 <= number <= 1400

# Test for edge case with maximum value set to 1
def test_edge_case():
    address = Address()
    street_number = address.street_number(maximum=1)
    assert isinstance(street_number, str)
    number = int(street_number)
    assert 1 <= number <= 1

# Test for invalid input with a non-integer maximum value
def test_invalid_input():
    address = Address()
    with pytest.raises(TypeError):
        address.street_number(maximum="not an integer")
