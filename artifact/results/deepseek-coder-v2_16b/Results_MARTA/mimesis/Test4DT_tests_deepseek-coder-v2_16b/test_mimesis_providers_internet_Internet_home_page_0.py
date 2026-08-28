
import pytest
from mimesis.providers.internet import Internet
from mimesis.enums import TLDType

# Fixture to create an instance of the Internet class for testing
@pytest.fixture(scope="module")
def internet_instance():
    return Internet()

# Test function to check if a valid specific TLD is returned correctly

# Test function to check if an invalid TLD raises an error or returns a default value
def test_invalid_input_none_tld(internet_instance):
    home_page = internet_instance.home_page()  # No specific TLD provided
    assert isinstance(home_page, str), "Expected a string representation of the home page URL"
    assert home_page.startswith('https://'), f"Home page should start with 'https://', but got: {home_page}"