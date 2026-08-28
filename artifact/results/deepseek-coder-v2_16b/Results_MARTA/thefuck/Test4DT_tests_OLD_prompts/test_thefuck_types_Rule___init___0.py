
import pytest
from unittest.mock import patch
from thefuck.types import Rule

# Test initialization of Rule class
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
