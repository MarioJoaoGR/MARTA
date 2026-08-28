
import pytest
from httpie.context import Environment
import sys
from pathlib import Path

def test_default_init():
    env = Environment()
    assert hasattr(env, 'is_windows')
    assert hasattr(env, 'config_dir')
    assert hasattr(env, 'stdin')
    assert hasattr(env, 'stdout')
    assert hasattr(env, 'stderr')
    assert hasattr(env, 'colors')
    assert hasattr(env, 'program_name')
    assert env.is_windows is not None
    assert isinstance(env.config_dir, Path)
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert isinstance(env.colors, int)
    assert isinstance(env.program_name, str)

def test_custom_devnull():
    with open('/dev/null', 'w') as devnull:
        env = Environment(devnull=devnull)
        assert env._devnull == devnull

def test_invalid_input():
    with pytest.raises(AssertionError):
        env = Environment(non_existent_attr='value')
