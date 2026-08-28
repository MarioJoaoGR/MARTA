
import pytest
from thefuck.shells.generic import Generic

# Fixture to create an instance of Generic for testing
@pytest.fixture
def generic_instance():
    return Generic()

# Test initialization of Generic class
def test_initialization(generic_instance):
    assert hasattr(generic_instance, 'friendly_name')
    assert getattr(generic_instance, 'friendly_name') == 'Generic Shell'

# Test get_history method with no "fuck" command in history
def test_get_history_no_fuck(generic_instance):
    # Mock a list of commands without "fuck"
    generic_instance._history = ["ls", "cd", "pwd"]