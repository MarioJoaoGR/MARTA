
import pytest
from thefuck.shells.generic import Generic
import shlex



def test_valid_input():
    generic_shell = Generic()
    command = "ls -l"
    expected_output = ["ls", "-l"]
    assert generic_shell.split_command(command) == expected_output