
import pytest
from mimesis.providers.person import Person
import re  # Importing re module for regular expression operations

# Assuming the Person class and its methods are correctly implemented as per the provided documentation

@pytest.fixture
def person_provider():
    return Person(locale='en', seed=42)

def test_username_default_template(person_provider):
    username = person_provider.username()
    assert isinstance(username, str), "Username should be a string"
    assert len(username) > 0, "Username should not be empty"
    assert re.search(r'[A-Z]', username) or re.search(r'[a-z]', username), "Username must contain at least one uppercase or lowercase letter"

def test_username_custom_template_valid(person_provider):
    template = 'U.d'
    username = person_provider.username(template)
    assert isinstance(username, str), "Username should be a string"
    assert len(username) > 0, "Username should not be empty"
    assert re.search(r'[A-Z]', username), "Username must contain at least one uppercase letter"