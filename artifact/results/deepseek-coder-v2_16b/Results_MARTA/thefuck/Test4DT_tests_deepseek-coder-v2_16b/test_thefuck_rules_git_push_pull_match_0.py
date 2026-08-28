
import pytest
from thefuck.rules.git_push_pull import match
from thefuck.types import Command


def test_valid_push_not_rejected():
    command = Command(script='git push origin main', output='To https://github.com/user/repo.git')
    assert match(command) is False
