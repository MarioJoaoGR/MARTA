
import pytest
from unittest.mock import patch

def get_new_command(command):
    command_parts = command.split()
    if 'rm' in command_parts:
        index = command_parts.index('rm') + 1
        command_parts.insert(index, '-r')
    return ' '.join(command_parts)

@pytest.mark.parametrize("command, expected", [
    ("rm file.txt", "rm -r file.txt"),
    ("cp old new && rm .", "cp old new && rm -r ."),
    ("ls -l", "ls -l")
])
def test_get_new_command(command, expected):
    assert get_new_command(command) == expected

@pytest.mark.parametrize("command", [""])
def test_edge_case_empty_string(command):
    assert get_new_command(command) == command

@pytest.mark.parametrize("command, expected", [
    ("ls -l", "ls -l"),
    ("rm file.txt", "rm -r file.txt")
])
def test_invalid_input(command, expected):
    assert get_new_command(command) == expected
