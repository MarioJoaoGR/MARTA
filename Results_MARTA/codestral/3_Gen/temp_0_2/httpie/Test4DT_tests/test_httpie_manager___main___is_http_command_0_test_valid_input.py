
import pytest
from unittest.mock import patch
from httpie.manager.cli import COMMANDS
from httpie.manager.__main__ import Environment, is_http_command

def test_valid_input():
    with patch('httpie.manager.cli.COMMANDS', {'get': True}):
        env = Environment()
        args = ['get', 'http://example.com']
        result = is_http_command(args, env)
        assert not result  # Since 'get' is a top-level command, it should return False

    with patch('httpie.manager.cli.COMMANDS', {'get': True}):
        env = Environment()
        args = ['other_command', 'http://example.com']
        result = is_http_command(args, env)
        assert result  # Since 'other_command' is not in COMMANDS, it should return True and attempt to parse the arguments
