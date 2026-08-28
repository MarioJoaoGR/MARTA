
import pytest
from thefuck.shells.generic import Generic


def test_valid_input_single():
    commands = ['ls']
    generic_shell = Generic()
    combined_commands = generic_shell.and_(*commands)
    assert combined_commands == 'ls'

def test_valid_input_empty():
    commands = []
    generic_shell = Generic()
    combined_commands = generic_shell.and_(*commands)
    assert combined_commands == ''