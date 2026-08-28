
import pytest
from mimesis.providers.person import Person

# Initialize the Person class for testing
@pytest.fixture
def person():
    return Person()

def test_default_usage(person):
    # Test default usage of gender method without parameters
    result = person.gender()
    assert result in ['Male', 'Female'], f"Expected 'Male' or 'Female', but got {result}"

def test_iso5218_representation(person):
    # Test using iso5218 parameter to get the ISO 5218 code representation
    with pytest.raises(TypeError):
        person.gender(iso5218=True)

def test_symbol_representation(person):
    # Test using symbol parameter to get the gender symbol representation
    with pytest.raises(TypeError):
        person.gender(symbol=True)
