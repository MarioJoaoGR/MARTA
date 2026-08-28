
import pytest
from thefuck.rules.sudo_command_from_user_path import _get_command_name


def test_normal_output():
    command = type('Command', (object,), {'output': 'sudo: unknownuser: command not found'})()
    assert _get_command_name(command) == "unknownuser"

def test_no_match():
    command = type('Command', (object,), {'output': 'This is a normal output without any error message.'})()
    assert _get_command_name(command) is None

def test_empty_output():
    command = type('Command', (object,), {'output': ''})()
    assert _get_command_name(command) is None