# Module: mimesis.providers.person
import pytest
from mimesis.providers.person import Person

# Initialize the Person class for testing
@pytest.fixture
def person():
    return Person()

# Test case 1: Default parameters (minimum=1.5, maximum=2.0)
def test_height_default(person):
    height = person.height()
    assert isinstance(height, str), "Expected a string representation of the height"
    value = float(height)
    assert 1.5 <= value <= 2.0, f"Height should be between 1.5 and 2.0, but got {value}"
    assert len(height.split('.')[1]) == 2, "Expected two decimal places in the height"

# Test case 2: Specifying custom minimum and maximum values
def test_height_custom_range(person):
    height = person.height(minimum=1.6, maximum=2.1)
    assert isinstance(height, str), "Expected a string representation of the height"
    value = float(height)
    assert 1.6 <= value <= 2.1, f"Height should be between 1.6 and 2.1, but got {value}"
    assert len(height.split('.')[1]) == 2, "Expected two decimal places in the height"

# Test case 3: Using the method with no parameters (uses default values)
def test_height_no_parameters(person):
    height = person.height()
    assert isinstance(height, str), "Expected a string representation of the height"
    value = float(height)
    assert 1.5 <= value <= 2.0, f"Height should be between 1.5 and 2.0, but got {value}"
    assert len(height.split('.')[1]) == 2, "Expected two decimal places in the height"
