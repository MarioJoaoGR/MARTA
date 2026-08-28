
import pytest
from thefuck.rules.aws_cli import match
from thefuck.types import Command


def test_match_without_usage_or_maybe_you_meant():
    command = Command("An unexpected error occurred.", "echo 'Hello, World!'")
    assert match(command) == False

def test_match_with_only_usage():
    command = Command("This is a usage error.", "echo 'Hello, World!'")
    assert match(command) == False

def test_match_with_only_maybe_you_meant():
    command = Command("maybe you meant something else.", "echo 'Hello, World!'")
    assert match(command) == False