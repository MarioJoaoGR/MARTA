
import pytest
from thefuck.shells.generic import Generic

# Initialize the class instance
@pytest.fixture
def generic_instance():
    return Generic()

# Test cases for from_shell method with no aliases defined
def test_no_aliases(generic_instance):
    command_script = 'ls -l'
    expanded_command = generic_instance.from_shell(command_script)
    assert expanded_command == 'ls -l'

# Test cases for from_shell method with defined aliases
def test_defined_aliases(generic_instance):
    # Assuming 'ls' is an alias for 'command_name' in the aliases dictionary
    generic_instance.aliases = {'ls': 'command_name'}
    command_script = 'ls -l'
    expanded_command = generic_instance.from_shell(command_script)