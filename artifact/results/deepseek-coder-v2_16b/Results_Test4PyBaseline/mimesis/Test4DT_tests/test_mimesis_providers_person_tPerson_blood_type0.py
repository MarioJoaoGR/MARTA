# Module: mimesis.providers.person
import pytest
from mimesis.providers.person import Person

# Assuming BLOOD_GROUPS is a predefined list of blood types in the actual implementation
BLOOD_GROUPS = ['A+', 'B-', 'AB+', 'O-']

@pytest.fixture
def person():
    return Person()

def test_blood_type(person):
    """Test that a random blood type is returned."""
    blood_type = person.blood_type()
    assert blood_type in BLOOD_GROUPS, f"Expected blood type to be one of {BLOOD_GROUPS}, but got {blood_type}"
