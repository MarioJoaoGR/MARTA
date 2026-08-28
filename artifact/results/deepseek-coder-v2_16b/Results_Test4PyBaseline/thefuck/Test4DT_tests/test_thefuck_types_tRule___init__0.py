# Module: thefuck.types
# test_rule.py
from thefuck.types import Rule

def match_example(command):
    return command.text == "old_command"

def get_new_command_example(command):
    return "new_command"

def test_basic_rule_initialization():
    rule = Rule("ExampleRule", match_example, get_new_command_example, True, None, 1, False)
    assert rule.name == "ExampleRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 1
    assert rule.requires_output is False

def test_rule_with_specific_side_effect():
    def side_effect_example(command, new_command):
        print(f"Executing corrected command: {new_command}")
    
    rule = Rule("ExampleRule", match_example, get_new_command_example, True, side_effect_example, None, False)
    assert rule.name == "ExampleRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect == side_effect_example
    assert rule.priority is None
    assert rule.requires_output is False

def test_rule_with_high_priority():
    rule = Rule("ExampleRule", match_example, get_new_command_example, True, None, 10, False)
    assert rule.name == "ExampleRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 10
    assert rule.requires_output is False

def test_rule_with_specific_match_and_get_new_command():
    def match_specific(command):
        return command.text == "specific_command"
    
    def get_new_command_specific(command):
        return ["new_specific_command1", "new_specific_command2"]
    
    rule = Rule("SpecificRule", match_specific, get_new_command_specific, True, None, 1, False)
    assert rule.name == "SpecificRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 1
    assert rule.requires_output is False
