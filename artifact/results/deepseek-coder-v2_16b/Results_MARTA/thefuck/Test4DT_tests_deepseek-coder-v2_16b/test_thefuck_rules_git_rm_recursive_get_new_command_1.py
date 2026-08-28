
import pytest
from unittest.mock import patch

def get_new_command(command):
    command_parts = command.split()
    index = command_parts.index('rm') + 1 if 'rm' in command_parts else -1
    if index != -1:
        command_parts.insert(index, '-r')
    return ' '.join(command_parts)

@pytest.mark.parametrize("command, expected", [
    ("rm file.txt", "rm -r file.txt"),
    ("cp old new && rm .", "cp old new && rm -r ."),
])
def test_valid_input(command, expected):
    assert get_new_command(command) == expected

def test_edge_case_empty_string():
    assert get_new_command("") == ""

@pytest.mark.parametrize("command", ["ls -l"])
def test_invalid_input(command):
    assert get_new_command(command) == command
