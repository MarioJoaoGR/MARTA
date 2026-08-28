
# Module: thefuck.types
# test_rule.py
from thefuck.types import Rule

def test_equality():
    def match_example(command):
        return command.text == "match_command"
    
    def get_new_command_example(command):
        return "get_new_command"
    
    rule1 = Rule("ExampleRule", match_example, get_new_command_example, True, None, 1, False)
    rule2 = Rule("ExampleRule", match_example, get_new_command_example, True, None, 1, False)
    rule3 = Rule("DifferentRule", match_example, get_new_command_example, True, None, 1, False)
    
    assert rule1 == rule2
    assert not (rule1 == rule3)

def test_equality_with_different_attributes():
    def match_example(command):
        return command.text == "match_command"
    
    def get_new_command_example(command):
        return "get_new_command"
    
    rule1 = Rule("ExampleRule", match_example, get_new_command_example, True, None, 1, False)
    rule2 = Rule("ExampleRule", lambda command: False, get_new_command_example, True, None, 1, False)
    
    assert not (rule1 == rule2)

def test_equality_with_different_types():
    def match_example(command):
        return command.text == "match_command"
    
    def get_new_command_example(command):
        return "get_new_command"
    
    rule1 = Rule("ExampleRule", match_example, get_new_command_example, True, None, 1, False)
    assert not (rule1 == "not a Rule instance")

def test_equality_with_none():
    def match_example(command):
        return command.text == "match_command"
    
    def get_new_command_example(command):
        return "get_new_command"
    
    rule1 = Rule("ExampleRule", match_example, get_new_command_example, True, None, 1, False)
    assert not (rule1 == None)
