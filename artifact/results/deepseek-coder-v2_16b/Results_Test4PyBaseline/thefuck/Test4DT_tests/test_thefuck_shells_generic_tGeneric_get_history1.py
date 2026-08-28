
import pytest
from thefuck.shells.generic import Generic

# Fixture to create an instance of Generic for testing
@pytest.fixture
def generic_instance():
    return Generic()

# Test initialization of Generic class
def test_initialization(generic_instance):
    assert hasattr(generic_instance, 'friendly_name')

# Test get_history method with empty history
def test_get_history_empty(generic_instance):
    generic_instance._get_history_lines = lambda: []  # Mocking the _get_history_lines method to return an empty list