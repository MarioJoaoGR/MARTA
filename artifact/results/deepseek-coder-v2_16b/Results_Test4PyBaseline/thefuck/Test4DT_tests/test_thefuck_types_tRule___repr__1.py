
import pytest
from thefuck.types import Rule

# Test initialization with default values
def test_rule_initialization():
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

# Test initialization with custom match and get new command functions
def test_rule_initialization_custom():
    def custom_match(command):
        return command.text == "custom_old_command"
    
    def custom_get_new_command(command):
        return ["custom_new_command1", "custom_new_command2"]
    
    rule = Rule("CustomRule", custom_match, custom_get_new_command, False, None, 5, True)
    
    assert rule.name == "CustomRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert not rule.enabled_by_default
    assert rule.side_effect is None
    assert rule.priority == 5
    assert rule.requires_output

# Test initialization with side effect function
def test_rule_initialization_with_side_effect():
    def default_match(command):
        return command.text == "default_old_command"
    
    def default_get_new_command(command):
        return "default_new_command"
    
    rule = Rule("DefaultRule", default_match, default_get_new_command, True, lambda command, new_command: print(f"Applying side effect for {new_command}"), 10, False)
    
    assert rule.name == "DefaultRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default
    assert callable(rule.side_effect)
    assert rule.priority == 10
    assert not rule.requires_output

# Test initialization with requires output
def test_rule_initialization_with_requires_output():
    def requires_output_match(command):
        return command.text == "requires_output_old_command"
    
    def requires_output_get_new_command(command):
        return "requires_output_new_command"
    
    rule = Rule("RequiresOutputRule", requires_output_match, requires_output_get_new_command, True, None, 1, True)
    
    assert rule.name == "RequiresOutputRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default
    assert rule.side_effect is None
    assert rule.priority == 1
    assert rule.requires_output

# Test initialization with high priority and side effect function
def test_rule_initialization_with_high_priority():
    def high_priority_match(command):
        return command.text == "high_priority_old_command"
    
    def high_priority_get_new_command(command):
        return "high_priority_new_command"
    
    rule = Rule("HighPriorityRule", high_priority_match, high_priority_get_new_command, True, lambda command, new_command: print(f"Applying side effect for {new_command}"), 1, False)
    
    assert rule.name == "HighPriorityRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default
    assert callable(rule.side_effect)
    assert rule.priority == 1
    assert not rule.requires_output

# Test __repr__ method
def test_rule_repr():
    def match_example(command):
        return command.text == "old_command"
    
    def get_new_command_example(command):
        return "new_command"
    
    rule = Rule("ExampleRule", match_example, get_new_command_example, True, None, 1, False)
    
    expected_repr = 'Rule(name=ExampleRule, match=<function test_rule_initialization.<locals>.match_example at ...>, get_new_command=<function test_rule_initialization.<locals>.get_new_command_example at ...>, enabled_by_default=True, side_effect=None, priority=1, requires_output=False)'