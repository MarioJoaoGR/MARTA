
import pytest
from unittest.mock import patch, MagicMock
from thefuck.rules.brew_install import _get_similar_formula, match
from thefuck.types import Command

def test_match_proper_command_with_unavailable_error():
    command_object = Command("brew install unavailable_formula", "Error: No available formula for unavailable_formula")
    with patch('thefuck.rules.brew_install._get_similar_formula', return_value=True):
        assert match(command_object) is True

def test_match_proper_command_with_available_error():
    command_object = Command("brew install available_formula", "Error: No such file or directory - unavailable_formula")
    with patch('thefuck.rules.brew_install._get_similar_formula', return_value=False):
        assert match(command_object) is False

def test_match_improper_command():
    command_object = Command("brew", "Some other output")
    assert match(command_object) is False

def test_match_proper_command_without_error():
    command_object = Command("brew install available_formula", "")
    assert match(command_object) is False
