
import pytest
from unittest.mock import patch
import sys
from pathlib import Path
from httpie.context import Environment, DEFAULT_CONFIG_DIR

# Test default initialization of the Environment class
def test_default_initialization():
    env = Environment()
    assert isinstance(env, Environment)
    assert env.is_windows == bool(sys.platform == 'win32')
    assert isinstance(env.config_dir, Path)
    assert env.stdin is sys.stdin
    assert isinstance(env.stdin_isatty, bool)
    assert env.stdout is sys.stdout
    assert isinstance(env.stdout_isatty, bool)
    assert env.stderr is sys.stderr
    assert isinstance(env.stderr_isatty, bool)
    assert env.colors == 256