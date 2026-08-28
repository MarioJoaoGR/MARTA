
import pytest
from mimesis.providers.address import Address

# Assuming CALLING_CODES is a predefined list of calling codes in the Address class
CALLING_CODES = ['1', '44', '61', '33', '81']  # Example calling codes, replace with actual data if available

@pytest.fixture(scope="module")
def address():
    return Address()

def test_calling_code_default_locale(address):
    """Test the default locale for calling code."""
    assert isinstance(address.calling_code(), str)