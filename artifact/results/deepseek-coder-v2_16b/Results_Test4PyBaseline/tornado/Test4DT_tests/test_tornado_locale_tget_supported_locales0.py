
# Module: tornado.locale
from typing import Iterable  # Importing Iterable from typing module
from tornado.locale import get_supported_locales

# Test cases for the get_supported_locales function

def test_get_supported_locales():
    supported_locales = get_supported_locales()
    assert isinstance(supported_locales, Iterable), f"Expected an iterable but got {type(supported_locales)}"

def test_get_supported_locales_type():
    # Test the return type of the function
    supported_locales = get_supported_locales()
    assert isinstance(supported_locales, Iterable), f"Expected an iterable but got {type(supported_locales)}"

def test_get_supported_locales_not_empty():
    # Test that the returned list is not empty
    supported_locales = get_supported_locales()
    assert len(supported_locales) > 0, "Expected at least one supported locale"

def test_get_supported_locales_contains_expected_locales():
    # Assuming _supported_locales contains some expected locale codes for testing
    supported_locales = get_supported_locales()