# Module: thefuck.shells.generic
import pytest
from thefuck.shells.generic import Generic

# Fixture to create an instance of Generic for testing
@pytest.fixture
def generic_instance():
    return Generic()

# Test case for the friendly name property
def test_friendly_name(generic_instance):
    assert generic_instance.friendly_name == 'Generic Shell'

# Test case for the from_shell method (assuming no aliases are defined)
@pytest.mark.parametrize("command_script, expected", [
    ('ls -l', 'ls -l'),  # Assuming no aliases are defined
])
def test_from_shell(generic_instance, command_script, expected):
    expanded_command = generic_instance.from_shell(command_script)
    assert expanded_command == expected

# Test case for the to_shell method (assuming no shell-specific preparation is required)
@pytest.mark.parametrize("command_script, expected", [
    ('ls -l', 'ls -l'),  # Assuming no shell-specific preparation is required
])
def test_to_shell(generic_instance, command_script, expected):
    prepared_command = generic_instance.to_shell(command_script)
    assert prepared_command == expected

# Test case for the get_aliases method (since it returns an empty dictionary by default)
def test_get_aliases(generic_instance):
    assert generic_instance.get_aliases() == {}
