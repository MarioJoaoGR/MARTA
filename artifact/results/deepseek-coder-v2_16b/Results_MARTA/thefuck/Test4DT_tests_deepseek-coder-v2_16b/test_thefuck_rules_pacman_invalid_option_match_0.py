
import pytest
from thefuck.rules.pacman_invalid_option import match
from thefuck.types import Command



def test_no_invalid_option():
    command = Command("echo 'Hello, World!'", "Hello, World!")
    assert not match(command)