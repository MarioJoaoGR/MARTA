
import pytest
from unittest.mock import patch, MagicMock
from thefuck.types import Rule

# Test for rule matching with a command containing "old_command"
def test_rule_match_with_old_command():
    def match(command):
        return "old_command" in command.script

    def get_new_command(command):
        return "new_command"

    rule = Rule("example_rule", match, get_new_command, True, None, 10, False)

    class Command:
        def __init__(self, script):
            self.script = script
        @property
        def output(self):
            return None

    command = Command("some old_command")
    assert rule.is_match(command) is True

# Test for rule matching with a command not containing "old_command"