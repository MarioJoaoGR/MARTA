
import pytest
from mimesis import Address

# Initialize an instance of the Address class with default locale
@pytest.fixture(scope="module")
def address():
    return Address()

# Test that a random state is returned when calling state() without arguments
def test_state_default(address):
    state = address.state()
    assert isinstance(state, str), "Expected a string representation of a state"

# Test that an abbreviated state code is returned when calling state(abbr=True)
def test_state_abbr(address):
    abbr_state = address.state(abbr=True)
    assert len(abbr_state) == 2, "Expected the abbreviation to be two characters long"
    assert isinstance(abbr_state, str), "Expected a string representation of an abbreviated state"

# Test that a random prefecture is returned when calling prefecture()
def test_prefecture(address):
    prefecture = address.prefecture()