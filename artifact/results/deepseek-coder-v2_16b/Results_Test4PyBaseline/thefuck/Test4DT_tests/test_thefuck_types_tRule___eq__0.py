# Module: thefuck.types
# test_rule.py
from thefuck.types import Rule

def test_basic_usage():
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

def test_custom_matching_and_command_generation():
    def custom_match(command):
        return command.text == "custom_command"
    
    def get_new_command_example(command):
        return ["new_command1", "new_command2"]
    
    rule = Rule("CustomRule", custom_match, get_new_command_example, True, None, 2, False)
    
    assert rule.name == "CustomRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 2
    assert not rule.requires_output

def test_using_default_values_and_side_effects():
    def match_default(command):
        return True
    
    def get_new_command_default(command):
        return "default_command"
    
    side_effect = lambda command, new_command: print(f"Side effect for {new_command}")
    rule = Rule("DefaultRule", match_default, get_new_command_default, False, side_effect, 1, True)
    
    assert rule.name == "DefaultRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert not rule.enabled_by_default
    assert callable(rule.side_effect)
    assert rule.priority == 1
    assert rule.requires_output

def test_high_priority_and_requires_output():
    def high_priority_match(command):
        return command.text == "high_priority_command"
    
    def get_new_command_high_priority(command):
        return ["high_priority_command_replacement"]
    
    rule = Rule("HighPriorityRule", high_priority_match, get_new_command_high_priority, True, None, 10, True)
    
    assert rule.name == "HighPriorityRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 10
    assert rule.requires_output

def test_no_side_effect_and_low_priority():
    def low_priority_match(command):
        return command.text == "low_priority_command"
    
    def get_new_command_low_priority(command):
        return ["low_priority_command_replacement"]
    
    rule = Rule("LowPriorityRule", low_priority_match, get_new_command_low_priority, True, lambda command, new_command: None, 1, False)
    
    assert rule.name == "LowPriorityRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert callable(rule.side_effect)
    assert rule.priority == 1
    assert not rule.requires_output
