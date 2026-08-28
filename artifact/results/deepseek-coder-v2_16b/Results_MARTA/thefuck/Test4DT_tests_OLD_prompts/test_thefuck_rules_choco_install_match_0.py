
import pytest
from unittest.mock import patch, MagicMock
from thefuck.rules.choco_install import match
from thefuck.types import Command

# Test for rule matching with a command containing 'choco install' or 'cinst' and output including 'Installing the following packages'
def test_valid_case_choco_install():
    command_obj = Command("choco install", "Installing the following packages")
    assert match(command_obj) is True

# Test for rule matching with a command containing 'cinst' and output including 'Installing the following packages'
def test_valid_case_cinst():
    command_obj = Command("cinst", "Installing the following packages")
    assert match(command_obj) is True

# Test for rule not matching when the command does not start with 'choco install' or contain 'cinst' in its script, even if output includes 'Installing the following packages'
def test_invalid_input():
    command_obj = Command("npm install", "Installing the following packages")
    assert match(command_obj) is False
