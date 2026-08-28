
import pytest
from mimesis.providers.person import Person
import random
import string
import hashlib

# Fixture to create a Person instance for testing
@pytest.fixture
def person():
    return Person()

# Test cases for the password method
def test_default_password(person):
    default_password = person.password()
    assert isinstance(default_password, str), "Default password should be a string"
    assert len(default_password) == 8, "Default password length should be 8 characters"

def test_custom_length_password(person):
    custom_length_password = person.password(length=16)
    assert isinstance(custom_length_password, str), "Custom length password should be a string"
    assert len(custom_length_password) == 16, "Custom length password length should be 16 characters"

def test_hashed_password(person):
    hashed_password = person.password(hashed=True)
    assert isinstance(hashed_password, str), "Hashed password should be a string"