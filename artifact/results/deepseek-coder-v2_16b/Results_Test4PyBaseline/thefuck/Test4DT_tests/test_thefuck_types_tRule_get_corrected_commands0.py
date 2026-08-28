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

def test_custom_side_effect():
    def side_effect_function(command, message):
        print(f"Executing corrected command: {command.text} with side effect: {message}")
    
    rule = Rule("ExampleRule", lambda command: command.text == "old_command", lambda command: ["new_command"], True, side_effect_function, 1, False)
    
    assert rule.name == "ExampleRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert callable(rule.side_effect)
    assert rule.priority == 1
    assert not rule.requires_output

def test_without_side_effect():
    rule = Rule("ExampleRule", lambda command: command.text == "old_command", lambda command: ["new_command"], True, None, 1, False)
    
    assert rule.name == "ExampleRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 1
    assert not rule.requires_output

def test_using_functions_as_parameters():
    rule = Rule("ExampleRule", lambda command: command.text == "old_command", lambda command: ["new_command"], True, None, 1, False)
    
    assert rule.name == "ExampleRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 1
    assert not rule.requires_output

def test_using_specific_command_object():
    class Command:
        def __init__(self, text):
            self.text = text
    
    command = Command("old_command")
    
    rule = Rule("ExampleRule", lambda command: command.text == "old_command", lambda command: ["new_command"], True, None, 1, False)
    
    assert rule.name == "ExampleRule"
    assert callable(rule.match)
    assert callable(rule.get_new_command)
    assert rule.enabled_by_default is True
    assert rule.side_effect is None
    assert rule.priority == 1
    assert not rule.requires_output
