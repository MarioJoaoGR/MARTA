
import pytest
from unittest.mock import patch, MagicMock
from thefuck.types import Rule

# Test for rule initialization with default parameters
def test_rule_initialization():
    def match(command):
        return "old_command" in command.script

    def get_new_command(command):
        return "new_command"

    rule = Rule("example_rule", match, get_new_command, True, None, 10, False)
    assert rule.name == "example_rule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 10
    assert not rule.requires_output

# Test for rule initialization with custom parameters
def test_rule_initialization_with_custom_parameters():
    def custom_match(command):
        return command.script == "custom_old_command"

    def custom_get_new_command(command):
        return ["custom_new_command"]

    rule = Rule("custom_rule", custom_match, custom_get_new_command, False, None, 5, True)
    assert rule.name == "custom_rule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert not rule.enabled_by_default
    assert rule.side_effect is None
    assert rule.priority == 5
    assert rule.requires_output

# Test for creating a Rule instance from a path (mocking the import process)
@patch('thefuck.types.load_source')
def test_rule_from_path(mock_load_source):
    mock_load_source.return_value = MagicMock()
    mock_load_source.return_value.match = lambda command: "old_command" in command.script
    mock_load_source.return_value.get_new_command = lambda command: "new_command"
    mock_load_source.return_value.enabled_by_default = True
    mock_load_source.return_value.side_effect = None
    mock_load_source.return_value.priority = 10
    mock_load_source.return_value.requires_output = False

    from pathlib import Path
    rule = Rule.from_path(Path('rules/example_rule.py'))
    assert isinstance(rule, Rule)
    assert rule.name == "example_rule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 10
    assert not rule.requires_output
