
import pytest
from unittest.mock import patch
from thefuck.shells.generic import Generic

# Test case for expanding aliases in a command script
def test_expand_aliases():
    with patch('thefuck.shells.generic.Generic.get_aliases', return_value={'view': 'ls'}):
        generic_shell = Generic()
        command_script = "view -l"
        expanded_command = generic_shell._expand_aliases(command_script)
        assert expanded_command == "ls -l"

# Test case for handling a command without an alias
def test_no_alias():
    with patch('thefuck.shells.generic.Generic.get_aliases', return_value={}):
        generic_shell = Generic()
        command_script = "view -l"
        expanded_command = generic_shell._expand_aliases(command_script)
        assert expanded_command == "view -l"
