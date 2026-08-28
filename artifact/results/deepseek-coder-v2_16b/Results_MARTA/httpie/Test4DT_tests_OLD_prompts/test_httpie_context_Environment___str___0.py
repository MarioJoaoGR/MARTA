
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment
import sys
from pathlib import Path

# Test 1: Default Initialization

# Test 2: Custom `devnull` Parameter
def test_custom_devnull():
    with patch('sys.stdin', new=MagicMock()):
        devnull_file = MagicMock()
        env = Environment(devnull=devnull_file)
        assert env._devnull == devnull_file

# Test 3: Custom Configuration Directory
def test_custom_config_dir():
    with patch('sys.stdin', new=MagicMock()):
        custom_config_dir = Path('/custom/config/directory')
        env = Environment(config_dir=custom_config_dir)
        assert env.config_dir == custom_config_dir

# Test 4: Redirection of Standard Error to a File-like Object for Quiet Mode
def test_redirection_stderr():
    with patch('sys.stdin', new=MagicMock()):
        devnull_file = MagicMock()
        env = Environment(devnull=devnull_file)
        assert env._devnull == devnull_file

# Test 5: Overriding Multiple Parameters
def test_overriding_multiple_parameters():
    with patch('sys.stdin', new=MagicMock()):
        custom_config_dir = Path('/custom/config/directory')
        devnull_file = MagicMock()
        env = Environment(devnull=devnull_file, config_dir=custom_config_dir)
        assert env._devnull == devnull_file
        assert env.config_dir == custom_config_dir

# Test 6: Initialization with Specific `stdin` and `stdout`
def test_specific_stdin_stdout():
    with patch('sys.stdin', new=MagicMock()):
        stdin_mock = MagicMock()
        stdout_mock = MagicMock()
        env = Environment(stdin=stdin_mock, stdout=stdout_mock)
        assert env.stdin == stdin_mock
        assert env.stdout == stdout_mock