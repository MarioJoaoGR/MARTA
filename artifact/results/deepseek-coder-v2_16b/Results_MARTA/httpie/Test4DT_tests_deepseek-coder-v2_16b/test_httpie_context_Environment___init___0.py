
import pytest
from httpie.context import Environment
import sys
from pathlib import Path

# Test default initialization
def test_default_initialization():
    env = Environment()
    assert hasattr(env, 'is_windows')
    assert hasattr(env, 'config_dir')
    assert hasattr(env, 'stdin')
    assert hasattr(env, 'stdout')
    assert hasattr(env, 'stderr')
    assert hasattr(env, 'colors')
    assert hasattr(env, 'program_name')
    assert env.is_windows is not None
    assert env.config_dir == Path.home() / '.httpie'
    assert env.stdin is sys.stdin
    assert env.stdout is sys.stdout
    assert env.stderr is sys.stderr
    assert env.colors == 256
    assert env.program_name == 'http'

# Test custom devnull

# Test custom config directory
def test_custom_config_dir():
    with pytest.raises(AssertionError):
        env = Environment(config_dir='/custom/config/directory')
        assert hasattr(env, 'config_dir')
        assert env.config_dir == Path('/custom/config/directory')