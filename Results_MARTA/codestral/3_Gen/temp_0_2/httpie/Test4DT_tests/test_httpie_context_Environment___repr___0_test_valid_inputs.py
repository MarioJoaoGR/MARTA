
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment
import sys
from pathlib import Path

@pytest.fixture
def setup_environment():
    with patch('sys.stdin', new=MagicMock()), \
         patch('sys.stdout', new=MagicMock()), \
         patch('sys.stderr', new=MagicMock()):
        # Create an instance of Environment with default values
        env = Environment()
        yield env

def test_valid_inputs(setup_environment):
    env = setup_environment
    
    assert isinstance(env, Environment)
    assert env.is_windows == (sys.platform == 'win32')
    assert isinstance(env.config_dir, Path)
    assert env.stdin is not None
    assert isinstance(env.stdout, type(sys.stdout))
