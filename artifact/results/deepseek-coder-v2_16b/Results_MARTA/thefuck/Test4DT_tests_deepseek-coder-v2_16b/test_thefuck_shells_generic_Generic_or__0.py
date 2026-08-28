
import pytest
from thefuck.shells.generic import Generic

def test_or_method():
    generic_shell = Generic()
    combined_command = generic_shell.or_("echo Hello", "ls -l")
    assert combined_command == "echo Hello || ls -l"

def test_or_with_none():
    generic_shell = Generic()
    combined_command = generic_shell.or_()
    assert combined_command == ""

def test_or_with_one_command():
    generic_shell = Generic()
    combined_command = generic_shell.or_("echo Hello")
    assert combined_command == "echo Hello"
