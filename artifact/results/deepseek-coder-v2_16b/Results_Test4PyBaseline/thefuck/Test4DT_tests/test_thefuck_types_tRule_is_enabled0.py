
# Module: thefuck.types
# test_types.py
from thefuck.types import Rule

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

def test_rule_initialization_with_custom_settings():
    def match_custom(command):
        return command.script == "old_command"
    
    def get_new_command_custom(command):
        return ["new_command", "another_command"]
    
    rule = Rule("CustomRule", match_custom, get_new_command_custom, False, None, 2, True)
    assert rule.name == "CustomRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is False
    assert rule.side_effect is None
    assert rule.priority == 2
    assert rule.requires_output

def test_rule_initialization_with_specific_parameters():
    def match_specific(command):
        return command.text == "specific_command"
    
    def get_new_command_specific(command):
        return ["specific_replacement"]
    
    rule = Rule("SpecificRule", match_specific, get_new_command_specific, True, lambda command, new_command: print(f"Applying side effect for {new_command}"), 3, False)
    assert rule.name == "SpecificRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert callable(rule.side_effect)
    assert rule.priority == 3
    assert not rule.requires_output

def test_is_enabled():
    def match_example(command):
        return command.text == "old_command"
    
    def get_new_command_example(command):
        return "new_command"
    
    rule = Rule("ExampleRule", match_example, get_new_command_example, True, None, 1, False)