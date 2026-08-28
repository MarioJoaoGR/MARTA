
import pytest
from mimesis.providers.person import Person

# Initialize the Person class with a seed for reproducibility
@pytest.fixture
def person():
    return Person(seed=12345)

# Test default usage of the weight method
def test_default_weight(person):
    weight = person.weight()
    assert isinstance(weight, int), "Expected an integer value"
    assert 38 <= weight <= 90, f"Weight should be between 38 and 90, but got {weight}"

# Test custom range usage of the weight method
def test_custom_range_weight(person):
    weight = person.weight(minimum=40, maximum=80)
    assert isinstance(weight, int), "Expected an integer value"
    assert 40 <= weight <= 80, f"Weight should be between 40 and 80, but got {weight}"

# Test the method with a different seed to ensure reproducibility
def test_reproducible_weight(person):
    first_run = person.weight()
    second_run = person.weight()