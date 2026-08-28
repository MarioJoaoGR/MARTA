
import pytest
from thefuck.rules.git_add_force import match
from thefuck.types import Command

# Test for valid case where command contains 'add' in script parts and includes specific message about force adding

# Test for invalid case where command does not contain 'add' in script parts but includes specific message about force adding
def test_invalid_no_add():
    command_obj = Command(['something', 'else'], 'Use -f if you really want to add them.')
    assert match(command_obj) is False

# Test for invalid case where command contains 'add' in script parts but does not include specific message about force adding
def test_invalid_no_message():
    command_obj = Command(['add', 'something'], 'Some other message')
    assert match(command_obj) is False