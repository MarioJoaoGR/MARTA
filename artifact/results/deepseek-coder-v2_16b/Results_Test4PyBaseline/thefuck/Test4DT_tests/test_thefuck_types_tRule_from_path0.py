
# Module: thefuck.types
import pytest
from thefuck.types import Rule

# Test initialization with default values
def test_rule_initialization_with_default_values():
    def match_example(command):
        return command.text == "old_command"
    
    def get_new_command_example(command):
        return "new_command"
    
    rule = Rule("ExampleRule", match_example, get_new_command_example, True, None, 1, False)
    
    assert rule.name == "ExampleRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 1
    assert not rule.requires_output

# Test initialization with custom values
def test_rule_initialization_with_custom_values():
    def match_custom(command):
        return command.text == "specific_command"
    
    def get_new_command_custom(command):
        return ["new_specific_command"]
    
    rule = Rule("CustomRule", match_custom, get_new_command_custom, False, lambda cmd, new_cmd: print(f"Applying side effect for {cmd.text} -> {new_cmd}"), 2, True)
    
    assert rule.name == "CustomRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert not rule.enabled_by_default
    assert callable(rule.side_effect)
    assert rule.priority == 2