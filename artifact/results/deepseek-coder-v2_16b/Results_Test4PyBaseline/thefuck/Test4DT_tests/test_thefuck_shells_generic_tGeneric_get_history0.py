
import pytest
from thefuck.shells.generic import Generic

# Fixture to create an instance of Generic for testing
@pytest.fixture
def generic_instance():
    return Generic()

# Test initialization of Generic class
def test_initialization(generic_instance):
    assert hasattr(generic_instance, 'friendly_name')