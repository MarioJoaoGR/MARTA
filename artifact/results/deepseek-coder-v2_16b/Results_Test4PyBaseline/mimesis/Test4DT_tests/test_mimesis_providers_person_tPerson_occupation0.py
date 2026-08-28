
import pytest
from mimesis import BaseProvider
from mimesis.providers.person import Person

# Assuming the module is correctly imported and named as expected

@pytest.fixture
def person():
    return Person()

def test_occupation(person):
    job = person.occupation()
    assert isinstance(job, str), "Expected occupation to be a string"

def test_reseed(person):
    initial_seed = person.seed
    original_job = person.occupation()
    
    # Reseed without changing the seed value
    person.reseed()
    reseeded_job = person.occupation()
    