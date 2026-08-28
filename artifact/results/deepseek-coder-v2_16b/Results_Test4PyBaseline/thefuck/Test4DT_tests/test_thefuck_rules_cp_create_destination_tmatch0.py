
import pytest
from thefuck.rules.cp_create_destination import match

# Test cases for the `match` function

def test_match_no_such_file():
    command_obj = type('Command', (object,), {'output': 'ls: no-such-file: No such file or directory'})()
    assert "No such file or directory" in command_obj.output

def test_match_cp_directory_does_not_exist():
    another_command_obj = type('Command', (object,), {'output': 'cp: directory /path/to/directory: does not exist'})()
    assert another_command_obj.output.startswith("cp: directory") and another_command_obj.output.rstrip().endswith("does not exist")

def test_match_neither_error():
    third_command_obj = type('Command', (object,), {'output': 'echo Hello, World!'})()
    assert not ("No such file or directory" in third_command_obj.output) and not (third_command_obj.output.startswith("cp: directory") and third_command_obj.output.rstrip().endswith("does not exist"))
